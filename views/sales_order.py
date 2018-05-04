from flask import render_template

from services.database import db_service


def view_items():
    context = {}
    context['title'] = 'Items'
    context['headers'] = ['ID', 'BOB ID SO Item', 'Sales Order', 'SO Status',
                          'Delivery Type', 'Unit Price', 'Tax Amount',
                          'Paid Price', 'Name', 'SKU', 'Created', 'Updated',
                          'Last Change', 'Original Unit Price',
                          'Shipping Type', 'Real Delivery Date',
                          'BOB ID Supplier', 'Is Marketplace']
    context['rows'] = db_service.get_items()
    
    return render_template('sales_order/items.html', context=context)


def view_status():
    context = {}
    context['title'] = 'Item Status'
    context['headers'] = ['ID', 'OMS Function', 'Status', 'Description',
                          'Deprecated', 'Updated']
    context['rows'] = db_service.get_status()
    
    return render_template('sales_order/status.html', context=context)


def view_history():
    context = {}
    context['title'] = 'Item Status History'
    context['headers'] = ['ID', 'Item Name', 'Last Status', 'Created At']
    context['rows'] = db_service.get_history()
    
    return render_template('sales_order/history.html', context=context)
