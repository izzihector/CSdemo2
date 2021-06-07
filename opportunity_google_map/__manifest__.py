# -*- coding: utf-8 -*-
##############################################################################
#
# Part of Aardug. (Website: www.aardug.nl).
# See LICENSE file for full copyright and licensing details.
#
##############################################################################
{
    'name' : 'Opportunity Google Map',
    'version': '14.0.0.1',
    'summary': 'Map View For Opportunity',
    'category': 'Map View',
    'description': """Opportunity locate on google map""",
    'author': 'Aardug, Arjan Rosman',
    'website': 'http://www.aardug.nl/',
    'depends': ['contacts', 'base_geolocalize', 'crm', 'lead_category', 'web_map'],
    'data': [
        'data/data.xml',
        'views/assets.xml',
        'views/crm_stage_view.xml',
        'views/crm_lead_view.xml',
        'views/lead_category_view.xml',
        'views/map_view.xml',
    ],
}
