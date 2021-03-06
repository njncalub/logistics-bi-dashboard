from flask import Flask, request, send_from_directory

from core import settings
from views import home
from views import analysis as analysis_view
from views import custom as custom_view
from views import sales_order as sales_order_view


app = Flask('Logistiko')


def run_server(*args, **kwargs):
    options = {
        'host': '0.0.0.0',
        'port': '5000',
        'debug': False,
        'secret_key': 'SET-YOUR-SECRET-KEY',
    }
    options.update(kwargs)
    
    # set the SECRET_KEY before loading the config
    SECRET_KEY = options['secret_key']
    
    app.run(host=options['host'],
            port=options['port'],
            debug=options['debug'])


def set_app_routes():
    app.add_url_rule(rule='/favicon.ico', endpoint='favicon',
                     view_func=home.favicon, methods=['GET'])
    
    app.add_url_rule(rule='/', endpoint='homepage', view_func=home.homepage,
                     methods=['GET'])
    
    # for analysis
    app.add_url_rule(rule='/regions', endpoint='analysis:regions',
                     view_func=analysis_view.view_regions, methods=['GET'])
    app.add_url_rule(rule='/packages', endpoint='analysis:packages',
                     view_func=analysis_view.view_packages, methods=['GET'])
    
    # for sales order
    app.add_url_rule(rule='/items', endpoint='sales_order:items',
                     view_func=sales_order_view.view_items, methods=['GET'])
    app.add_url_rule(rule='/status', endpoint='sales_order:status',
                     view_func=sales_order_view.view_status, methods=['GET'])
    app.add_url_rule(rule='/history', endpoint='sales_order:history',
                     view_func=sales_order_view.view_history, methods=['GET'])
    
    # for custom situations
    app.add_url_rule(rule='/custom/1.5', endpoint='custom:1.5',
                     view_func=custom_view.view_situation_1_5, methods=['GET'])
    app.add_url_rule(rule='/custom/1.6', endpoint='custom:1.6',
                     view_func=custom_view.view_situation_1_6, methods=['GET'])
    app.add_url_rule(rule='/custom/1.7', endpoint='custom:1.7',
                     view_func=custom_view.view_situation_1_7, methods=['GET'])
    app.add_url_rule(rule='/custom/2.1', endpoint='custom:2.1',
                     view_func=custom_view.view_situation_2_1, methods=['GET'])
    app.add_url_rule(rule='/custom/2.2', endpoint='custom:2.2',
                     view_func=custom_view.view_situation_2_2, methods=['GET'])
    app.add_url_rule(rule='/custom/2.3', endpoint='custom:2.3',
                     view_func=custom_view.view_situation_2_3, methods=['GET'])
    app.add_url_rule(rule='/custom/2.4', endpoint='custom:2.4',
                     view_func=custom_view.view_situation_2_4, methods=['GET'])
    app.add_url_rule(rule='/custom/2.5', endpoint='custom:2.5',
                     view_func=custom_view.view_situation_2_5, methods=['GET'])
    app.add_url_rule(rule='/custom/2.6', endpoint='custom:2.6',
                     view_func=custom_view.view_situation_2_6, methods=['GET'])
    
    # rest api
    # app.add_url_rule(rule='/api/', endpoint=)

set_app_routes()


if __name__ == '__main__':
    run_server(host=settings.SERVER_HOST,
               port=settings.SERVER_PORT,
               debug=settings.DEBUG,
               secret_key=settings.SECRET_KEY)
