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
    def zonnepanelen_parser(self, emailBody):
        """This Method returns plain text dict for
        Template Zonnepanelen.
        """
        plain_text_body = tools.html2plaintext(emailBody)
        newdict = {}
        a = find_between_r(plain_text_body, 'Leadgegevens', 'Situatie').split('\n')
        if len(a) > 1:
            addresindex = [i for i, s in enumerate(a) if 'Straat' in s]
            if addresindex and addresindex[0]:
                newdict['Adres:'] = a[addresindex[0]+1] + ' ' + a[addresindex[0]+5]

            postcodeindex = [i for i, s in enumerate(a) if 'Postcode' in s]
            if postcodeindex and postcodeindex[0]:
                newdict['Postcode:'] = a[postcodeindex[0]+1]

            cityindex = [i for i, s in enumerate(a) if 'Plaats' in s]
            if cityindex and cityindex[0]:
                newdict['Plaats:'] = a[cityindex[0]+1]

            telephoneindex = [i for i, s in enumerate(a) if 'Telefoon' in s]
            if telephoneindex and telephoneindex[0]:
                newdict['Telefoon:'] = a[telephoneindex[0]+1]

            # mobileindex = [i for i, s in enumerate(a) if 'Mobiel' in s]
            # if mobileindex and mobileindex[0]:
            #     plain_mobile = a[mobileindex[0]+1].replace('*', '')
            #     newdict['Mobiel:'] = a[mobileindex[0]+2].replace('*', '')

            emailindex = [i for i, s in enumerate(a) if 'E-mail' in s]
            if emailindex and emailindex[0]:
                newdict['E-mail:'] = a[emailindex[0]+1]

            first_name = ''
            last_name = ''

            first_index = [i for i, s in enumerate(a) if 'Voornaam' in s]
            if first_index and first_index[0]:
                first_name = a[first_index[0]+1].replace('*', '')

            last_index = [i for i, s in enumerate(a) if 'Achternaam' in s]
            if last_index and last_index[0]:
                last_name = a[last_index[0]+1].replace('*', '')

            newdict['Voornaam:'] = first_name + ' ' +  last_name
        return newdict

    @api.model
    def zonnepanelen_condition(self, mailMessage, emailBody):
        """Condition for Zonnepanelen template."""
        return (mailMessage.xaa_aa_company == 'zonnepanelen' or
                'zonnepanelen' in emailBody)

    @api.model
    def register_company_parser(self):
        """Register Zonnepanelen Parser Mappin in main."""
        parsers = super(CrmLead, self).register_company_parser()
        parsers.append(
            (15,
             self.zonnepanelen_condition,
             self.zonnepanelen_parser))
        return parsers
