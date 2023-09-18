{
    'name': "Real_Estate",
    'version': '16.0.0.0.0',
    'depends': ['base'],
    'category': 'Category',
    'description': "Real Estate",
    'website': 'https://www.odoo.com/page/Real_Estate',
    'installable': True,
    'application': True,
    'auto_install': False,
    'data': [
        'security/ir.model.access.csv',
        'views/estate_property_views.xml',
        'views/estate_property_type_views.xml',
        'views/estate_property_tag_views.xml',
        'views/estate_property_offer_views.xml',
        'views/estate_menus.xml',
    ],
}
