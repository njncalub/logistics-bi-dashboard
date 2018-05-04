from flask import Flask, request, send_from_directory

from views import home
from views import analysis as analysis_view
from views import sales_order as sales_order_view

def run_server(*args, **kwargs):
    options = {
        'host': '0.0.0.0',
        'port': '5000',
        'debug': True,
        'secret_key': 'SET-YOUR-SECRET-KEY',
    }
    options.update(kwargs)
    
    app = Flask('Logistiko')
    
    # set the SECRET_KEY before loading the config
    SECRET_KEY = options['secret_key']
    
    set_app_routes(app)
    
    app.run(host=options['host'],
            port=options['port'],
            debug=options['debug'])


def set_app_routes(app):
    app.add_url_rule(rule='/favicon.ico', endpoint='favicon',
                     view_func=home.favicon, methods=['GET'])
    
    app.add_url_rule(rule='/', endpoint='homepage', view_func=home.homepage,
                     methods=['GET'])
    
    # for analysis
    app.add_url_rule(rule='/regions', endpoint='analysis.regions',
                     view_func=analysis_view.view_regions, methods=['GET'])
    app.add_url_rule(rule='/packages', endpoint='analysis.packages',
                     view_func=analysis_view.view_packages, methods=['GET'])
    
    # for sales order
    app.add_url_rule(rule='/items', endpoint='sales_order.items',
                     view_func=sales_order_view.view_items, methods=['GET'])
    app.add_url_rule(rule='/status', endpoint='sales_order.status',
                     view_func=sales_order_view.view_status, methods=['GET'])
    app.add_url_rule(rule='/history', endpoint='sales_order.history',
                     view_func=sales_order_view.view_history, methods=['GET'])
