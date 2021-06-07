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
        return ""


class CrmLead(models.Model):
    _inherit = 'crm.lead'

    @api.model
    def slimster_parser(self, emailBody):
        '''
            This Method returns plain text dict by parsing raw text of mail for 
            Template slimster
        '''
        plain_text_body = tools.html2plaintext(emailBody)
        newdict = {}
        result = find_between_r(plain_text_body, 'Bron', 'Concullega').split('\n')
        if len(result) > 1:
            werkzaamheden = ''
            materiaal = ''
            model = ''
            uitvoermoment = ''
            opdrachtomschrijving = ''
            gespreksverslag = ''
            construction_year = ''
            type_of_house = ''
            type_of_insulation = ''
            type_of_roof = ''
            property_owned = ''
            execution_time = ''
            job_description = ''
            type_of_application = ''
            annual_power_consumption = ''
            buy_or_rent = ''
            placement = ''
            # lead details
            naamindex = [i for i, s in enumerate(result) if 'Naam:' in s]
            if naamindex and naamindex[0]:
                if 'Mevr' in result[naamindex[0]+1]:
                    titleMevrouw = self.env.ref('create_crm_lead.res_partner_title_mevrouw')
                    newdict['title'] = titleMevrouw.id if titleMevrouw else False
                if 'Dhr' in result[naamindex[0]+1]:
                    titleHeer = self.env.ref('create_crm_lead.res_partner_title_heer')
                    newdict['title'] = titleHeer.id if titleHeer else False
                else:
                    titleFamilie = self.env.ref('create_crm_lead.res_partner_title_familie')
                    newdict['title'] = titleFamilie.id if titleFamilie else False

                naam = result[naamindex[0]+1].split('.')
                if len(naam) > 1:
                    newdict['Naam:'] = naam[1]
                else:
                    newdict['Naam:'] = result[naamindex[0]+1] or ''
            telefoonindex = [i for i, s in enumerate(result) if 'Telefoon:' in s]
            if telefoonindex and telefoonindex[0]:
                telefoon = result[telefoonindex[0]+1].split(' ') 
                newdict['Telefoon:'] = telefoon[0] if len(telefoon) == 2 else ''
            emailindex = [i for i, s in enumerate(result) if 'E-mailadres:' in s]
            if emailindex and emailindex[0]:
                newdict['E-mailadres:'] = result[emailindex[0]+1] or ''
            adresindex = [i for i, s in enumerate(result) if 'Adres:' in s]
            if adresindex and adresindex[0]:
                newdict['Adres:'] = result[adresindex[0]+1] or '' 
                city_zip = result[adresindex[0]+2].split(' ')
                newdict['Plaats:'] = str(city_zip[2]+ ' '+ city_zip[3]).replace(', NL', '')
                newdict['Postcode:'] = str(city_zip[0]+ ' ' + city_zip[1])
            # lead description
            constructionyearindex = [i for i, s in enumerate(result) if 'Bouwjaar:' in s]
            constructionyearValue = ''
            if constructionyearindex and constructionyearindex[0]:
                constructionyearValue = result[constructionyearindex[0]+1] or ''
                if constructionyearValue:
                    construction_year = ': '.join(['Bouwjaar', constructionyearValue])
            typewoningindex = [i for i, s in enumerate(result) if 'Type woning:' in s]
            typewoningValue = ''
            if typewoningindex and typewoningindex[0]:
                typewoningValue = result[typewoningindex[0]+1] or ''
                if typewoningValue:
                    type_of_house = ': '.join(['Type woning', typewoningValue])
            typeofinsulationindex = [i for i, s in enumerate(result) if 'Soort isolatie:' in s]
            if typeofinsulationindex and typeofinsulationindex[0]:
                typeofinsulationValue = result[typeofinsulationindex[0]+1] or ''
                if typeofinsulationValue:
                    type_of_insulation = ': '.join(['Soort isolatie', typeofinsulationValue])
            roofindex = [i for i, s in enumerate(result) if 'Soort dak:' in s]
            if roofindex and roofindex[0]:
                roofValue = result[roofindex[0]+1] or ''
                if roofValue:
                    type_of_roof = ': '.join(['Soort dak', roofValue])
            property_owned_index = [i for i, s in enumerate(result) if 'Woning in bezit:' in s]
            if property_owned_index and property_owned_index[0]:
                propertyownedValue = result[property_owned_index[0]+1] or ''
                if propertyownedValue:
                    property_owned = ': '.join(['Woning in bezit', propertyownedValue])
            uitvoermomentindex = [i for i, s in enumerate(result) if 'Uitvoermoment:' in s]
            if uitvoermomentindex and uitvoermomentindex[0]:
                uitvoermomentValue = result[uitvoermomentindex[0]+1] or ''
                if uitvoermomentValue:
                    uitvoermoment = ': '.join(['Uitvoermoment', uitvoermomentValue])
            opdrachtomschrijvingindex = [i for i, s in enumerate(result) if 'Opdrachtomschrijving:' in s]
            if opdrachtomschrijvingindex and opdrachtomschrijvingindex[0]:
                opdrachtomschrijvingValue = result[opdrachtomschrijvingindex[0]+1] or ''
                if opdrachtomschrijvingValue:
                    opdrachtomschrijving = ': '.join(['Opdrachtomschrijving', opdrachtomschrijvingValue])
            gespreksverslagingindex = [i for i, s in enumerate(result) if 'Gespreksverslag:' in s]
            if gespreksverslagingindex and gespreksverslagingindex[0]:
                gespreksverslagValue = result[gespreksverslagingindex[0]+1] or ''
                if gespreksverslagValue:
                    gespreksverslag = ': '.join(['Gespreksverslag', gespreksverslagValue])
            # Add more details on descriptions
            typeofapplicationindex = [i for i, s in enumerate(result) if 'Type aanvraag:' in s]
            if typeofapplicationindex and typeofapplicationindex[0]:
                typeofapplicationValue = result[typeofapplicationindex[0]+1] or ''
                if typeofapplicationValue:
                    type_of_application = ': '.join(['Type aanvraag', typeofapplicationValue])
            powerconsumptionindex = [i for i, s in enumerate(result) if 'Jaarlijks stroomverbruik:' in s]
            if powerconsumptionindex and powerconsumptionindex[0]:
                powerconsumptionValue = result[powerconsumptionindex[0]+1] or ''
                if powerconsumptionValue:
                    annual_power_consumption = ': '.join(['Jaarlijks stroomverbruik', powerconsumptionValue])
            buy_rent_index = [i for i, s in enumerate(result) if 'Kopen of huren:' in s]
            if buy_rent_index and buy_rent_index[0]:
                buy_rent_Value = result[buy_rent_index[0]+1] or ''
                if buy_rent_Value:
                    buy_or_rent = ': '.join(['Kopen of huren', buy_rent_Value])
            placementindex = [i for i, s in enumerate(result) if 'Plaatsing:' in s]
            if placementindex and placementindex[0]:
                placementValue = result[placementindex[0]+1] or ''
                if placementValue:
                    placement = ': '.join(['Plaatsing', placementValue])
            # set description
            description = '\n\n'.join(
                [x for x in [construction_year, type_of_application, annual_power_consumption, buy_or_rent, placement, type_of_house, type_of_insulation, type_of_roof, property_owned, uitvoermoment, opdrachtomschrijving, gespreksverslag] if x])
            if description:
                newdict['Toelichting:'] = description
        return newdict

    @api.model
    def slimster_condition(self, mailMessage, emailBody):
        """Condition for slimster template."""
        return (mailMessage.xaa_aa_company == 'slimster' or
                'slimster' in emailBody)

    @api.model
    def register_company_parser(self):
        """Register slimster Parser Mappin in main."""
        parsers = super(CrmLead, self).register_company_parser()
        parsers.append(
            (6,
             self.slimster_condition,
             self.slimster_parser)
        )
        return parsers
