# -*- coding: utf-8 -*-
{
    'name': "Sale Order Production Status",
    'summary': "Imprimir Ticket con la Orden de Producción una vez que se condifrmó el pedido",
    'description': "This module add Production Status on Sales Order",
    'author': "Luis Magin Mata - TeletrabajoVE",
    'website': "http://www.teletrabajove.com",
    'category': 'Point of Sale',
    "license": "AGPL-3",
    "application": False,
    "installable": True,
    "auto_install": False,
    'version': '14.0.1',
    'depends': ['sale_management', 'sale_order_line_note', 'bi_product_dimension'],
    'data': [
        'views/sale_order_report_view.xml',
        'reports/report_production_order_templates.xml',
        'reports/report_production_order.xml',
    ],
    'qweb': [
        
    ],
}