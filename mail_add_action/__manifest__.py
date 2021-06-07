# -*- coding: utf-8 -*-
##############################################################################
#                                                                            #
# Part of Aardug. (Website: www.aardug.nl).                                  #
# See LICENSE file for full copyright and licensing details.                 #
#                                                                            #
##############################################################################


{
    'name': 'Add Server Action in Fetch-Mail.',
    'version': '14.0.1.0.0',
    'sequence': 4,
    'summary': 'Add Action',
    'description':
        """
        Add Server Action in Fetch-Mail to Manage Leads Records.
        """,
    'category': 'CRM',
    'author': "Aardug, Arjan Rosman",
    'website': "http://www.aardug.nl/",
    'support': 'arosman@aardug.nl',
    'depends': ['fetchmail'],
    'data': ['views/fetchmail_view.xml'],
    'installable': True,
    'application': False,
}
