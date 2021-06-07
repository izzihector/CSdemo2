# -*- encoding: utf-8 -*-


from bs4 import BeautifulSoup
import itertools
import logging
import re


from odoo import api, models, _
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
    def isolatieVergelijker_parser(self, emailBody):
        """This Method returns plain text dict for
        Template isolatievergelijker
        """
        plain_text_body = tools.html2plaintext(emailBody)
        newdict = {}
        result = find_between_r(plain_text_body, 'Contactgegevens', 'Beste').split('\n')
        if len(result) > 1:
            naamindex = [i for i, s in enumerate(result) if 'Naam' in s]
            if naamindex and naamindex[0]:
                naam = result[naamindex[0]+1].replace('*', '')
                if naam == ':':
                    newdict['Naam:'] = result[naamindex[0]+2].replace('*', '')
                else:
                    newdict['Naam:'] = naam
            telefoonindex = [i for i, s in enumerate(result) if 'Telefoon' in s]
            if telefoonindex and telefoonindex[0]:
                telefoon = result[telefoonindex[0]+1].replace('*', '')
                if telefoon == ':':
                    newdict['Telefoon:'] = result[telefoonindex[0]+2].split(' ')[0]
                else:
                    newdict['Telefoon:'] = telefoon
            mobileindex = [i for i, s in enumerate(result) if 'Mobiel' in s]
            if mobileindex and mobileindex[0]:
                mobile = result[mobileindex[0]+1].replace('*', '')
                if mobile == ':':
                    newdict['Mobiel:'] = result[mobileindex[0]+2].split(' ')[0]
                else:
                    newdict['Mobiel:'] = mobile
            emailindex = [i for i, s in enumerate(result) if 'E-mail' in s]
            if emailindex and emailindex[0]:
                email = result[emailindex[0]+1].replace('*', '')
                if email == ':':
                    newdict['E-mail:'] = result[emailindex[0]+3].replace('*', '')
                else:
                    newdict['E-mail:'] = email
            straatnaamindex = [i for i, s in enumerate(result) if 'Straatnaam' in s]
            if straatnaamindex and straatnaamindex[0]:
                straatnaam = result[straatnaamindex[0]+1].replace('*', '')
                if straatnaam == ':':
                    newdict['Straatnaam:'] = result[straatnaamindex[0]+2].replace('*', '')
                else:
                    newdict['Straatnaam:'] = straatnaam
            postcodeindex = [i for i, s in enumerate(result) if 'Postcode' in s]
            if postcodeindex and postcodeindex[0]:
                postcode = result[postcodeindex[0]+1].replace('*', '')
                if postcode == ':':
                    newdict['Postcode:'] = result[postcodeindex[0]+2].replace('*', '')
                else:
                    newdict['Postcode:'] = postcode
            plaatsindex = [i for i, s in enumerate(result) if 'Plaats' in s]
            if plaatsindex and plaatsindex[0]:
                plaats = result[plaatsindex[0]+1].replace('*', '')
                if plaats == ':':
                    newdict['Plaats:'] = result[plaatsindex[0]+2].replace('*', '')
                else:
                    newdict['Plaats:'] = plaats
            otherinfoindex = [i for i, s in enumerate(result) if 'Overige opmerkingen' in s]
            if otherinfoindex and otherinfoindex[0]:
                otherinfo = result[otherinfoindex[0]+1].replace('*', '')
                if otherinfo == ':':
                    newdict['Toelichting:'] = result[otherinfoindex[0]+2].replace('*', '')
                else:
                    newdict['Toelichting:'] = otherinfo
        return newdict

    @api.model
    def isolatieVergelijker_condition(self, mailMessage, emailBody):
        """Condition for isolatieVergelijker template."""
        return (mailMessage.xaa_aa_company == 'isolatievergelijker' or
                'isolatievergelijker' in emailBody)

    @api.model
    def register_company_parser(self):
        """Register isolatievergelijker Parser Mappin in main."""
        parsers = super(CrmLead, self).register_company_parser()
        parsers.append(
            (4,
             self.isolatieVergelijker_condition,
             self.isolatieVergelijker_parser))
        return parsers
