# -*- coding: utf-8 -*-
##############################################################################
#                                                                            #
# Part of Aardug. (Website: www.aardug.nl).                                  #
# See LICENSE file for full copyright and licensing details.                 #
#                                                                            #
##############################################################################

{
    "name": "Sequential Code for Project Formulier",
    "version": "14.0.0.1",
    "category": "Project Formulier",
    'author': "Aardug, Arjan Rosman",
    'website': 'http://www.aardug.nl/',
    'summary': '',
    'description': """
    main goal is set Sequential code for project formulier.
    1. Sequential Code Set for when new project formulier record create.
    2. Also Set Code for existing Project formulier when this module install.
    """,
    "depends": [
        "project_formulier",
    ],
    "data": [
        "data/formulier_sequence.xml",
        "views/formulier_view.xml",
    ],
    'installable': True,
    "pre_init_hook": "create_code_equal_to_id",
    "post_init_hook": "assign_old_sequences",
}
