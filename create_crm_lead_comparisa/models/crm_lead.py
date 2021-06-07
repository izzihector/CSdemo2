# -*- encoding: utf-8 -*-


import itertools
import logging


from bs4 import BeautifulSoup


from odoo import api, models
from odoo import tools


_logger = logging.getLogger(__name__)


def find_between_r(s, first, last):
    try:
        start = s.rindex(first) + len(first)
        return s[start:s.rindex(last, start)]
    except ValueError:
        return ""


class CrmLead(models.Model):
    _inherit = 'crm.lead'

    @api.model
    def comparisa_parser(self, emailBody):
        """This Method returns plain text dict for
        Template comparisa.
        """
        plain_text_body = tools.html2plaintext(emailBody)
        newdict = {}
        a = find_between_r(plain_text_body, 'Beste', 'Overige informatie:').split('\n')
        if len(a) > 1:
            addresindex = [i for i, s in enumerate(a) if 'Adres' in s]
            if addresindex and addresindex[0]:
                plain_adres = a[addresindex[0]+1].replace('*', '')
                if plain_adres == '':
                    newdict['Adres:'] = a[addresindex[0]+2].replace('*', '')
                else:
                    newdict['Adres:'] = adres[1]
            postcodeindex = [i for i, s in enumerate(a) if 'Postcode' in s]
            if postcodeindex and postcodeindex[0]:
                plain_postcode = a[postcodeindex[0]+1].replace('*', '')
                if plain_postcode == '':
                    newdict['Postcode:'] = a[postcodeindex[0]+2].replace('*', '')
                else:
                    newdict['Postcode:'] = plain_postcode[1]
            cityindex = [i for i, s in enumerate(a) if 'Plaats' in s]
            if cityindex and cityindex[0]:
                city = a[cityindex[0]+1].replace('*', '')
                if city == '':
                    newdict['Plaats:'] = a[cityindex[0]+2].replace('*', '')
                else:
                    newdict['Plaats:'] = city[1]
            telephoneindex = [i for i, s in enumerate(a) if 'Telefoon' in s]
            if telephoneindex and telephoneindex[0]:
                plain_telephone = a[telephoneindex[0]+1].replace('*', '')
                newdict['Telefoon:'] = a[telephoneindex[0]+2].replace('*', '')

            mobileindex = [i for i, s in enumerate(a) if 'Mobiel' in s]
            if mobileindex and mobileindex[0]:
                plain_mobile = a[mobileindex[0]+1].replace('*', '')
                newdict['Mobiel:'] = a[mobileindex[0]+2].replace('*', '')

            emailindex = [i for i, s in enumerate(a) if 'E-mail' in s]
            if emailindex and emailindex[0]:
                newdict['E-mail:'] = a[emailindex[0]+2].replace('*', '')

            title_name = ''
            titleindex = [i for i, s in enumerate(a) if 'Aanhef' in s]
            if titleindex and titleindex[0]:
                newdict['Aanhef:'] = a[titleindex[0]+2].replace('*', '')

            first_name = ''
            last_name = ''

            first_index = [i for i, s in enumerate(a) if 'Voornaam' in s]
            if first_index and first_index[0]:
                first_name = a[first_index[0]+2].replace('*', '')

            last_index = [i for i, s in enumerate(a) if 'Achternaam' in s]
            if last_index and last_index[0]:
                last_name = a[last_index[0]+2].replace('*', '')

            newdict['Voornaam:'] = first_name + ' ' +  last_name

            descriptionindex = [i for i, s in enumerate(a) if 'Extra informatie' in s]
            if descriptionindex and descriptionindex[0]:
                newdict['Toelichting:'] = a[descriptionindex[0]+2].replace('*', '')
        return newdict

    @api.model
    def comparisa_condition(self, mailMessage, emailBody):
        """Condition for zonnepanelenvergelijker template."""
        return (mailMessage.xaa_aa_company == 'Comparisa' or
                'Comparisa' in emailBody)

    @api.model
    def register_company_parser(self):
        """Register Zonnepanelenvergelijker Parser Mappin in main."""
        parsers = super(CrmLead, self).register_company_parser()
        parsers.append(
            (7,
             self.comparisa_condition,
             self.comparisa_parser))
        return parsers
