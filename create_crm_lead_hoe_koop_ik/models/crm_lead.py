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
    def hoe_koop_ik_parser(self, emailBody):
        """This Method returns plain text dict for
        Template Hoe koop ik hoekoopik.
        """
        plain_text_body = tools.html2plaintext(emailBody)
        newdict = {}
        a = find_between_r(plain_text_body, 'Geslacht:', '- Koopwijzer').split('\n')
        if len(a) > 1:
            addresindex = [i for i, s in enumerate(a) if 'Straat' in s]
            if addresindex and addresindex[0]:
                newdict['Adres:'] = a[addresindex[0]].replace('Straat:', '') + ' ' + a[addresindex[0]+1].replace('Huisnummer:', '')

            postcodeindex = [i for i, s in enumerate(a) if 'Postcode' in s]
            if postcodeindex and postcodeindex[0]:
                newdict['Postcode:'] = a[postcodeindex[0]].replace('Postcode:', '')

            cityindex = [i for i, s in enumerate(a) if 'Plaats' in s]
            if cityindex and cityindex[0]:
                newdict['Plaats:'] = a[cityindex[0]].replace('Plaats:', '')

            telephoneindex = [i for i, s in enumerate(a) if 'Telefoonnummer' in s]
            if telephoneindex and telephoneindex[0]:
                newdict['Telefoon:'] = a[telephoneindex[0]].replace('Telefoonnummer:', '')

            # mobileindex = [i for i, s in enumerate(a) if 'Mobiel' in s]
            # if mobileindex and mobileindex[0]:
            #     plain_mobile = a[mobileindex[0]+1].replace('*', '')
            #     newdict['Mobiel:'] = a[mobileindex[0]+2].replace('*', '')

            emailindex = [i for i, s in enumerate(a) if 'E-mail' in s]
            if emailindex and emailindex[0]:
                newdict['E-mail:'] = a[emailindex[0]].replace('E-mail:', '')

            nameindex = [i for i, s in enumerate(a) if 'Naam' in s]
            if nameindex and nameindex[0]:
                newdict['Voornaam:'] = a[nameindex[0]].replace('Naam:', '')
        return newdict

    @api.model
    def hoe_koop_ik_condition(self, mailMessage, emailBody):
        """Condition for Hoe koop ik hoekoopik template."""
        return (mailMessage.xaa_aa_company == 'hoe-koop-ik' or
                'hoe-koop-ik' in emailBody)

    @api.model
    def register_company_parser(self):
        """Register Hoe koop ik hoekoopik Parser Mappin in main."""
        parsers = super(CrmLead, self).register_company_parser()
        parsers.append(
            (17,
             self.hoe_koop_ik_condition,
             self.hoe_koop_ik_parser))
        return parsers
