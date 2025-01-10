# -*- coding: utf-8 -*-
{
    'name': "Modificaciones MartyDev",

    'summary': """
        Formatos y ajustes personalizados para MartyDev""",

    'description': """
        Formatos y ajustes personalizados para MartyDev
    """,

    'author': "Jose Marty",
    'website': "",

    # Categories can be used to filter modules in modules listing
    # Check https://github.com/odoo/odoo/blob/13.0/odoo/addons/base/data/ir_module_category_data.xml
    # for the full list
    'category': 'Formatos - Qweb - XML',
    'version': '1.0',

    # any module necessary for this one to work correctly
    #'depends': ['base','sale','account','l10n_latam_invoice_document'],
    'depends': ['base','sale','account'],

    # always loaded
    #'qweb': ['static/src/xml/pos_ticket.xml'],
    'data': [
        'reports/template_view.xml',
        #'reports/invoice_report.xml',
        #'reports/invoice_report_noh.xml',
        'reports/quotation_report.xml',
        #'reports/purchase_order.xml',
        #'reports/stock_picking.xml',
        'reports/view_report.xml',
        #'views/product_view.xml',
        #'security/ir.model.access.csv'
    ],
    'application': True,
    'installable':True,
}
