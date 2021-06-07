# -*- coding: utf-8 -*-
##############################################################################
#                                                                            #
# Part of Aardug. (Website: www.aardug.nl).                                  #
# See LICENSE file for full copyright and licensing details.                 #
#                                                                            #
##############################################################################


from odoo import api, tools, models


def find_between_r(s, first, last):
    try:
        start = s.rindex(first) + len(first)
        return s[start:s.rindex(last, start)]
    except ValueError:
        return ''


class CrmLead(models.Model):
    _inherit = 'crm.lead'

    @api.model
    def offertevergelijker_parser(self, emailBody):
        """This Method returns plain text dict for
        Template offertevergelijker.
        """
        plain_text_body = tools.html2plaintext(emailBody)
        newdict = {}
        # lead details
        result = find_between_r(plain_text_body, 'Klant gegevens', 'Zijn er nog vragen?').split('\n')
        if len(result) > 1:
            emailindex = [i for i, s in enumerate(result) if 'Email:' in s]
            if emailindex and emailindex[0]:
                finalemailindex = emailindex[0] + 1
                newdict['E-mail:'] = result[finalemailindex]
            telephoneindex = [i for i, s in enumerate(result) if 'Telefoon:' in s]
            if telephoneindex and telephoneindex[0]:
                finaltelephone = telephoneindex[0] + 1
                newdict['Telefoon:'] = result[finaltelephone]
            if result[1]:
                naam = ' '.join(result[1].split())
                newdict['Naam:'] = naam
            if result[2]:
                newdict['Straatnaam:'] = ' '.join(result[2].split())
            if result[3]:
                addressstring = result[3].split(' ')
                if len(addressstring) > 2:
                    newdict['Postcode:'] = addressstring[0]
                    newdict['Plaats:'] = addressstring[-1]
        # lead description
        descText = find_between_r(
            plain_text_body, 'Geachte', 'Klant gegevens').split('\n')
        if len(descText) > 1:
            # Comment this code because its not used for description.
            # huidige = ''
            # gewenste = ''
            # model = ''

            # huidigeindex = [i for i, s in enumerate(descText) if 'Huidige trapbekleding' in s]
            # if huidigeindex and huidigeindex[0]:
            #     print("come here !!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!1")
            #     huidigeValue = descText[huidigeindex[0]+1] or ''
            #     if huidigeValue:
            #         huidige = ': '.join(['Huidige trapbekleding', huidigeValue])
            # gewensteindex = [i for i, s in enumerate(descText) if 'Gewenste trapbekleding' in s]
            # if gewensteindex and gewensteindex[0]:
            #     print("come here !!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!2")
            #     gewensteValue = descText[gewensteindex[0]+1] or ''
            #     if gewensteValue:
            #         gewenste = ': '.join(['Huidige trapbekleding', gewensteValue])
            # modelindex = [i for i, s in enumerate(descText) if 'Model trap' in s]
            # if modelindex and modelindex[0]:
            #     print("come here !!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!3")
            #     modelValue = descText[modelindex[0]+1] or ''
            #     if modelValue:
            #         model = ': '.join(['Model trap', modelValue])
            # # set description
            # description = '\n\n'.join([x for x in [huidige, gewenste, model] if x])
            # if description:
            #     newdict['Toelichting:'] = description
            descriptionindex = [i for i, s in enumerate(descText) if 'Informatie / Opmerking' in s]
            if descriptionindex and descriptionindex[0]:
                plus_one = descriptionindex[0] + 1
                final_description = descText[plus_one:]
                newdict['Toelichting:'] = ''.join(final_description).replace('*', '')
        return newdict

    @api.model
    def offertevergelijker_condition(self, mailMessage, emailBody):
        """Condition for offertevergelijker template."""
        return (mailMessage.xaa_aa_company == 'offertevergelijker' or
                'offertevergelijker' in emailBody)

    @api.model
    def register_company_parser(self):
        """Register offertevergelijker Parser Mappin in main."""
        parsers = super(CrmLead, self).register_company_parser()
        parsers.append(
            (5,
             self.offertevergelijker_condition,
             self.offertevergelijker_parser)
        )
        return parsers
