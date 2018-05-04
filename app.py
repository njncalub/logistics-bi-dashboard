#!/usr/bin/env python
# -*- coding: utf-8 -*-

"""Logistiko: Business Intelligence Dashboard.

Usage:
  app.py (init|drop) db
  app.py load analysis <FILE>
  app.py load sales_order (--item|--status|--history) <FILE>
  app.py run
  app.py (-h | --help)
  app.py --version

Options:
  -h --help     Show this screen.
  --version     Show version.
"""


from docopt import docopt

from core import settings
from data.services import DataService
from parsers import (
    load_analysis_from_file,
    load_so_item_from_file,
    load_so_item_status_from_file,
    load_so_item_status_history_from_file,
)
from services.server import run_server


def main(args):
    db = DataService(engine=settings.DATABASE_URL)
    
    if args['init'] and args['db']:
        init_db(db_service=db)
    
    elif args['drop'] and args['db']:
        drop_db(db_service=db)
    
    elif args['load'] and args['analysis']:
        file_path = args['<FILE>']
        
        if not file_path:  # should automatically be handled by docopt
            return
        
        load_analysis(path=file_path, db_service=db)
    
    elif args['load'] and args['sales_order']:
        file_path = args['<FILE>']
        
        if not file_path:  # should automatically be handled by docopt
            return
        
        if args['--item']:
            load_sales_order(table='item', path=file_path, db_service=db)
        elif args['--status']:
            load_sales_order(table='item_status', path=file_path,
                             db_service=db)
        elif args['--history']:
            load_sales_order(table='item_status_history', path=file_path,
                             db_service=db)
    
    elif args['run']:
        run()


def init_db(db_service):
    print('Initializing the database...')
    db_service.init_database()


def drop_db(db_service):
    print('Dropping the database...')
    db_service.drop_database()


def load_analysis(path, db_service):
    print('Loading the analysis file...')
    load_analysis_from_file(path=path, db_service=db_service)


def load_sales_order(table, path, db_service):
    if table == 'item':
        load_so_item(path=path, db_service=db_service)
    elif table == 'item_status':
        load_so_item_status(path=path, db_service=db_service)
    elif table == 'item_status_history':
        load_so_item_status_history(path=path, db_service=db_service)


def load_so_item(path, db_service):
    print('Loading Sales Order Item...')
    load_so_item_from_file(path=path, db_service=db_service)


def load_so_item_status(path, db_service):
    print('Loading Sales Order Item Status...')
    load_so_item_status_from_file(path=path, db_service=db_service)


def load_so_item_status_history(path, db_service):
    print('Loading Sales Order Item Status History...')
    load_so_item_status_history_from_file(path=path, db_service=db_service)


def run():
    print('Running the server...')
    run_server(host=settings.SERVER_HOST,
           port=settings.SERVER_PORT,
           debug=settings.DEBUG,
           secret_key=settings.SECRET_KEY)

if __name__ == '__main__':
    args = docopt(__doc__, version='0.0.1')
    main(args=args)
