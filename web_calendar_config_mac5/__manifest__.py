{
    'name': 'Web Calendar Configuration',
    'version': '14.0.1.0',
    'summary': 'Web Calendar Configuration',
    'description': """
Web Calendar Configuration
==========================

This module allows you to configure web calendar according to your needs.
Calendar view settings are:

* Calendar time range
* Start (working) time
* Minutes per row/slot
* Show weekends
* Show week number
* First day of week
* Allow events overlap
* Disable drag and drop
* Disable resizing
* Default minutes when creating and resizing an event


Support
-------

Email: mac5_odoo@outlook.com


Keywords: Odoo Calendar Configuration, Odoo Web Calendar Configuration, Odoo Calendar Events
Odoo Calendar Meetings, Odoo Events, Odoo Meetings
""",
    'category': 'Calendar',
    'author': 'MAC5',
    'contributors': ['MAC5'],
    'website': 'https://apps.odoo.com/apps/modules/browse?author=MAC5',
    'depends': ['web_calendar_base_mac5'],
    'data': [
        'views/web_calendar_templates.xml',
        'views/res_config_views.xml',
    ],
    'installable': True,
    'application': False,
    'auto_install': False,
    'images': ['static/description/calendar_sample.png'],
    'price': 69.99,
    'currency': 'EUR',
    'support': 'mac5_odoo@outlook.com',
    'license': 'OPL-1',
}
