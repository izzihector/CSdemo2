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
    def valideas_parser(self, emailBody):
        """This Method returns plain text dict for
        Template comparisa.
        """
        plain_text_body = tools.html2plaintext(emailBody)
        newdict = {}
        a = find_between_r(plain_text_body, 'LeadID', 'Wij van Valideas').split('\n')
        if len(a) > 1:
            addresindex = [i for i, s in enumerate(a) if 'Adres' in s]
            if addresindex and addresindex[0]:
                plain_adres = a[addresindex[0]].replace('*', '')
                adres = plain_adres.split('Adres')
                if len(adres) == 2:
                    if '[' in adres[1]:
                        address_split = adres[1].split('[')
                        newdict['Adres:'] = address_split[0]
                    else:
                        newdict['Adres:'] = adres[1]
            postcodeindex = [i for i, s in enumerate(a) if 'Postcode' in s]
            if postcodeindex and postcodeindex[0]:
                plain_postcode = a[postcodeindex[0]].replace('*', '')
                postcode = plain_postcode.split('Postcode')
                if len(postcode) == 2:
                    if '[' in postcode[1]:
                        postcode_split = postcode[1].split('[')
                        newdict['Postcode:'] = postcode_split[0]
                    else:
                        newdict['Postcode:'] = postcode[1]

            cityindex = [i for i, s in enumerate(a) if 'Woonplaats' in s]
            if cityindex and cityindex[0]:
                plain_city = a[cityindex[0]].replace('*', '')
                city = plain_city.split('Woonplaats')
                if len(city) == 2:
                    if '[' in city[1]:
                        city_split = city[1].split('[')
                        newdict['Woonplaats:'] = city_split[0]
                    else:
                        newdict['Woonplaats:'] = city[1]

            telephoneindex = [i for i, s in enumerate(a)
                              if 'Telefoonnummer' in s]
            if telephoneindex and telephoneindex[0]:
                plain_telephone = a[telephoneindex[0]].replace('*', '')
                telephone = plain_telephone.split('Telefoonnummer')
                if len(telephone) == 2:
                    newdict['Telefoonnummer:'] = telephone[1]
            emailindex = [i for i, s in enumerate(a) if 'Email' in s]
            if emailindex and emailindex[0]:
                plain_email = a[emailindex[0]].replace('*', '')
                email = plain_email.split('Email')
                if len(email) == 2:
                    newdict['Email adres:'] = email[1]

            first_name = ''
            last_name = ''
            pre_fix = ''
            prefix_index = [i for i, s in enumerate(a) if 'Aanhef' in s]
            if prefix_index and prefix_index[0]:
                plain_prefix = a[prefix_index[0]].replace('*', '')
                prefix = plain_prefix.split('Aanhef')
                if len(prefix) == 2:
                    pre_fix = prefix[1]

            first_index = [i for i, s in enumerate(a) if 'Voornaam' in s]
            if first_index and first_index[0]:
                plain_first = a[first_index[0]].replace('*', '')
                voorname = plain_first.split('Voornaam')
                if len(voorname) == 2:
                    first_name = voorname[1]

            last_index = [i for i, s in enumerate(a) if 'Achternaam' in s]
            if last_index and last_index[0]:
                plain_last = a[last_index[0]].replace('*', '')
                achternaam = plain_last.split('Achternaam')
                if len(achternaam) == 2:
                    # newdict['Campagne:'] = naam[1]
                    last_name = achternaam[1]
            newdict['Voornaam:'] = pre_fix + first_name + last_name

            descindex = [i for i, s in enumerate(a) if 'Omschrijving' in s]
            if descindex and descindex[0]:
                plain_desc = a[descindex[0]].replace('*', '')
                extrainfo = plain_desc.split('Extra info')
                if len(extrainfo) == 2:
                    newdict['Toelichting:'] = extrainfo[1]
                if len(extrainfo) == 1:
                    newdict['Toelichting:'] = extrainfo[0]
        return newdict

    @api.model
    def valideas_condition(self, mailMessage, emailBody):
        """Condition for zonnepanelenvergelijker template."""
        return (mailMessage.xaa_aa_company == 'valideas' or
                'valideas' in emailBody)

    @api.model
    def register_company_parser(self):
        """Register Zonnepanelenvergelijker Parser Mappin in main."""
        parsers = super(CrmLead, self).register_company_parser()
        parsers.append(
            (8,
             self.valideas_condition,
             self.valideas_parser))
        return parsers
