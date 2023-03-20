# -*- coding: utf-8 -*- 


{
    'name': 'Algeria company accounting data',
    'author': 'Soft-integration',
    'application': False,
    'installable': True,
    'auto_install': False,
    'qweb': [],
    'description': False,
    'images': [],
    'version': '1.0.1.2',
    'category': 'Base',
    'demo': [],
    'depends': ['contacts'],
    'data': ['data/l10n_dz_company_data.xml',
             'security/ir.model.access.csv',
             'views/res_partner_views.xml',
             'views/res_company_views.xml',
             'views/report_invoice.xml'
             ],
    'license': 'LGPL-3',
}
