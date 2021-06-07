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
    def energie_control_parser(self, emailBody):
        """This Method returns plain text dict for
        Template energie-control.
        """
        plain_text_body = tools.html2plaintext(emailBody)
        newdict = {}
        a = find_between_r(plain_text_body, 'Naam:', 'Send from URL:').split('\n')
        if len(a) > 1:
            addresindex = [i for i, s in enumerate(a) if 'Straat' in s]
            if addresindex and addresindex[0]:
                newdict['Adres:'] = a[addresindex[0]].replace('Straat:', '')
            postcodeindex = [i for i, s in enumerate(a) if 'Postcode' in s]
            if postcodeindex and postcodeindex[0]:
                newdict['Postcode:'] = a[postcodeindex[0]].replace('Postcode:', '')
            cityindex = [i for i, s in enumerate(a) if 'Woonplaats' in s]
            if cityindex and cityindex[0]:
                newdict['Plaats:'] = a[cityindex[0]].replace('Woonplaats:', '')
            telephoneindex = [i for i, s in enumerate(a) if 'Telefoonnummer' in s]
            if telephoneindex and telephoneindex[0]:
                newdict['Telefoon:'] = a[telephoneindex[0]].replace('Telefoonnummer:', '')

            emailindex = [i for i, s in enumerate(a) if 'E-mailadres' in s]
            if emailindex and emailindex[0]:
                newdict['E-mail:'] = a[emailindex[0]].replace('E-mailadres:', '')
            newdict['Voornaam:'] = a[0]
            descriptionindex = [i for i, s in enumerate(a) if 'Opmerkingen' in s]
            if descriptionindex and descriptionindex[0]:
                newdict['Toelichting:'] = ''.join(a[descriptionindex[0]:]).replace('_', '')
        return newdict

    @api.model
    def energie_control_condition(self, mailMessage, emailBody):
        """Condition for energie-control template."""
        return (mailMessage.xaa_aa_company == 'energie-control' or
                'energie-control' in emailBody)

    @api.model
    def register_company_parser(self):
        """Register energie-control Parser Mappin in main."""
        parsers = super(CrmLead, self).register_company_parser()
        parsers.append(
            (18,
             self.energie_control_condition,
             self.energie_control_parser))
        return parsers
