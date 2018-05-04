#!/usr/bin/env python
# -*- coding: utf-8 -*-

"""Logistiko: Business Intelligence Dashboard.

Usage:
  app.py init_db
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
    
    if args['init_db']:
        db.init_database()
    
    elif args['load'] and args['analysis']:
        file_path = args['<FILE>']
        
        if not file_path:  # should automatically be handled by docopt
            return
        
        load_analysis(path=file_path)
    
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


def init_db():
    pass


def load_analysis(path):
    load_analysis_from_file(path)


def load_sales_order(table, path):
    if table == 'item':
        load_sales_order_item(path)
    elif table == 'item_status':
        load_sales_order_item_status(path)
    elif table == 'item_status_history':
        load_sales_order_item_status_history(path)


def load_sales_order_item(path):
    pass


def load_sales_order_item_status(path):
    pass


def load_sales_order_item_status_history(path):
    pass


def run():
    pass


if __name__ == '__main__':
    args = docopt(__doc__, version='0.0.1')
    main(args=args)
