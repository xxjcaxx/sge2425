# -*- coding: utf-8 -*-
{
    'name': "game",

    'summary': "Short (1 phrase/line) summary of the module's purpose",

    'description': """
Long description of module's purpose
    """,

    'author': "My Company",
    'website': "https://www.yourcompany.com",

    # Categories can be used to filter modules in modules listing
    # Check https://github.com/odoo/odoo/blob/15.0/odoo/addons/base/data/ir_module_category_data.xml
    # for the full list
    'category': 'Uncategorized',
    'version': '0.1',

    # any module necessary for this one to work correctly
    'depends': ['base'],

    # always loaded
    'data': [
        'security/ir.model.access.csv',
        'views/views.xml',
        'views/dragon.xml',
        'views/maps.xml',
        'views/game.xml',
        'views/templates.xml',
        'views/characters.xml',
        'views/object.xml',
        'views/typeCharacter.xml',
        'views/forja.xml',
        'views/object_type.xml',
        'views/model_player.xml',
        'views/teams.xml',
        'views/match.xml',
        'views/mercat_personatge.xml',
        'views/dragon_type.xml',
        'demo/demomaps.xml',
        'demo/democharacter.xml',
        'demo/demodragon.xml',
        'demo/demoforja.xml',
        'demo/typeCharacter.xml',
    ],

    # only loaded in demonstration mode
    'demo': [
        'demo/demo.xml',
    ],
}
