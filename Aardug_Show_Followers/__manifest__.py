# -*- coding: utf-8 -*-
##############################################################################
#
# Part of Aardug. (Website: www.aardug.nl).
# See LICENSE file for full copyright and licensing details.
#
##############################################################################

{
    'name' : 'Show Mail Followers',
    'version': '14.0.1.0',
    'summary': 'show Mail Followers in mail composer form',
    'category': 'products',
    'description': """ This Module Allowes to you See Followers on Mail Form""",
    'author': 'Aardug',
    'website': 'http://www.aardug.nl/',
    'support': 'info@aardug.nl',
    'depends': ['mail'],
    'data' : [
            'wizard/mail_compose_message_view.xml',
    ],
    'installable': True,
    'application': True,
}
