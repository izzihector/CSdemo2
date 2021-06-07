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
    def trustoo_parser(self, emailBody):
        """This Method returns plain text dict for
        Template Trustoo.
        """
        plain_text_body = tools.html2plaintext(emailBody)
        newdict = {}
        a = find_between_r(plain_text_body, 'Bekijk hieronder de details.', '').split('\n')
        while("" in a) :
            a.remove("")

        if len(a) > 1:
            postcodeindex = [i for i, s in enumerate(a) if 'Postcode en huisnummer' in s]
            if postcodeindex and postcodeindex[0]:
                newdict['Postcode:'] = a[postcodeindex[0]+1].split('- ')[1]
                newdict['Adres:'] = a[postcodeindex[0]+1].split('- ')[0]

            cityindex = [i for i, s in enumerate(a) if 'Plaats' in s]
            if cityindex and cityindex[0]:
                newdict['Plaats:'] = a[cityindex[0]+1]

            emailindex = [i for i, s in enumerate(a) if 'E-mail' in s]
            if emailindex and emailindex[0]:
                newdict['E-mail:'] = a[emailindex[0]+1]

            nameindex = [i for i, s in enumerate(a) if 'Naam' in s]
            if nameindex and nameindex[0]:
                newdict['Voornaam:'] = a[nameindex[0]+1]

            descriptionindex = [i for i, s in enumerate(a) if 'Eventuele opmerkingen' in s]
            if descriptionindex and descriptionindex[0]:
                newdict['Toelichting:'] = a[descriptionindex[0]+1]
        return newdict

    @api.model
    def trustoo_condition(self, mailMessage, emailBody):
        """Condition for Trustoo template."""
        return (mailMessage.xaa_aa_company == 'Trustoo' or
                'Trustoo' in emailBody)

    @api.model
    def register_company_parser(self):
        """Register Trustoo Parser Mappin in main."""
        parsers = super(CrmLead, self).register_company_parser()
        parsers.append(
            (13,
             self.trustoo_condition,
             self.trustoo_parser))
        return parsers
