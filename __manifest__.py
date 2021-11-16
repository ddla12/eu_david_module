# -*- coding: utf-8 -*-
{
    'name': "David Module",
    'summary': "Test what i've learned so far",
    'description': """
        This is a pet module, it allows to add pets to res.partner
    """,
    'author': "David Linarez",
    'website': "https://www.corpoeureka.com/web/",
    'version': '0.1',
    'depends': ['base'],
    'data': [
        'security/ir.model.access.csv',
        'data/species_data.xml'
        'views/pet_views.xml',
    ],
}
