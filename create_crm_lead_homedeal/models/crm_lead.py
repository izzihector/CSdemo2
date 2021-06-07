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
    def homedeal_parser(self, emailBody):
        """This Method returns plain text dict for
        Template homedeal.
        """
        plain_text_body = tools.html2plaintext(emailBody)
        newdict = {}
        a = find_between_r(plain_text_body, 'Contactinformatie:', 'Offerte details:').split('\n')
        if len(a) > 1:
            addresindex = [i for i, s in enumerate(a) if 'Adres' in s]
            if addresindex and addresindex[0]:
                newdict['Adres:'] = str(a[addresindex[0]+1]).partition('(')[0]
                # telephone[1].split(telephone[1].strip()[-3])
            postcodeindex = [i for i, s in enumerate(a) if 'Postcode' in s]
            if postcodeindex and postcodeindex[0]:
                newdict['Postcode:'] = a[postcodeindex[0]+1].replace('*', '')
            cityindex = [i for i, s in enumerate(a) if 'Plaats' in s]
            if cityindex and cityindex[0]:
                newdict['Plaats:'] = a[cityindex[0]+1].replace('*', '')
            telephoneindex = [i for i, s in enumerate(a) if 'Telefoon' in s]
            if telephoneindex and telephoneindex[0]:
                newdict['Telefoon:'] = a[telephoneindex[0]+1].replace('*', '')

            emailindex = [i for i, s in enumerate(a) if 'E-mail' in s]
            if emailindex and emailindex[0]:
                newdict['E-mail:'] = a[emailindex[0]+1].replace('*', '')

            naamindex = [i for i, s in enumerate(a) if 'Naam:' in s]
            if naamindex and naamindex[0]:
                if 'Mevr' in a[naamindex[0]+1]:
                    titleMevrouw = self.env.ref('create_crm_lead.res_partner_title_mevrouw')
                    newdict['title'] = titleMevrouw.id if titleMevrouw else False
                if 'Dhr' in a[naamindex[0]+1]:
                    titleHeer = self.env.ref('create_crm_lead.res_partner_title_heer')
                    newdict['title'] = titleHeer.id if titleHeer else False
                else:
                    titleFamilie = self.env.ref('create_crm_lead.res_partner_title_familie')
                    newdict['title'] = titleFamilie.id if titleFamilie else False

                naam = a[naamindex[0]+1].split('.')
                if len(naam) > 1:
                    newdict['Naam:'] = naam[1]
                else:
                    newdict['Naam:'] = a[naamindex[0]+1] or ''
            descriptionindex = [i for i, s in enumerate(a) if 'Extra informatie' in s]
            if descriptionindex and descriptionindex[0]:
                newdict['Toelichting:'] = a[descriptionindex[0]+2].replace('*', '')
        return newdict

    @api.model
    def homedeal_condition(self, mailMessage, emailBody):
        """Condition for homedeal template."""
        return (mailMessage.xaa_aa_company == 'homedeal' or
                'homedeal' in emailBody)

    @api.model
    def register_company_parser(self):
        """Register homedeal Parser Mappin in main."""
        parsers = super(CrmLead, self).register_company_parser()
        parsers.append(
            (10,
             self.homedeal_condition,
             self.homedeal_parser))
        return parsers
