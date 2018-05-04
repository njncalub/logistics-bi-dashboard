#!/usr/bin/env python
# -*- coding: utf-8 -*-

"""Logistiko: Business Intelligence Dashboard.

Usage:
  app.py (init|drop) db
  app.py load analysis <FILE>
  app.py load sales_order (--item|--item_status|--item_status_history) <FILE>
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
from parsers import load_analysis_from_file


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
            load_sales_order(table='item', path=file_path)
        elif args['--item_status']:
            load_sales_order(table='item_status', path=file_path)
        elif args['--item_status_history']:
            load_sales_order(table='item_status_history', path=file_path)
    
    elif args['run']:
        run()


def init_db(db_service):
    print('Initializing the database...')
    db_service.drop_database()
    db_service.init_database()


def drop_db(db_service):
    print('Dropping the database...')
    db_service.drop_database()


def load_analysis(path, db_service):
    print('Loading the analysis file...')
    load_analysis_from_file(path=path, db_service=db_service)


def load_sales_order(table, path):
    if table == 'item':
        load_sales_order_item(path)
    elif table == 'item_status':
        load_sales_order_item_status(path)
    elif table == 'item_status_history':
        load_sales_order_item_status_history(path)


def load_sales_order_item(path):
    print('Loading Sales Order Item...')


def load_sales_order_item_status(path):
    print('Loading Sales Order Item Status...')


def load_sales_order_item_status_history(path):
    print('Loading Sales Order Item Status History...')


def run():
    print('Running the server...')


if __name__ == '__main__':
    args = docopt(__doc__, version='0.0.1')
    main(args=args)
