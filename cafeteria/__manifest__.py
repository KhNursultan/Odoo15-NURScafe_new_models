# -*- coding: utf-8 -*-
{
    'name': "cafeteria",

    'summary': """
       A module that manages everything related to the company canteen""",

    'description': """
        A module that manages everything related to the company canteen
    """,

    'author': "Khamzabek Nursultan",
    'website': "http://www.nurs.com",

    # Categories can be used to filter modules in modules listing
    # Check https://github.com/odoo/odoo/blob/master/odoo/addons/base/module/module_data.xml
    # for the full list
    'category': 'Uncategorized',
    'version': '0.1',

    # any module necessary for this one to work correctly
    'depends': ['base', 'hr'],

    # always loaded
    'data': [
        # 'security/ir.model.access.csv',
        'views/views.xml',
        'views/templates.xml',
    ],
    # only loaded in demonstration mode
    'demo': [
        'demo/demo.xml',
    ],
    'installable':True,
    'application':True,
    'auto_install':False
}