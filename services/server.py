from flask import Flask, send_from_directory

from views import homepage, favicon


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
                     view_func=favicon, methods=['GET'])
    app.add_url_rule(rule='/', endpoint='homepage', view_func=homepage,
                     methods=['GET'])
