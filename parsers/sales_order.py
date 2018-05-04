import csv

from core.exceptions import InvalidFileException


def load_so_item_from_file(path, db_service):
    with open(path) as csv_file:
        csv_reader = csv.reader(csv_file)
        error_msg = 'Missing required header: {}'
        
        for i, row in enumerate(csv_reader, 1):
            data = {
                'id_sales_order_item': row[0],
                'bob_id_sales_order_item': row[1],
                'fk_sales_order': row[2],
                'fk_sales_order_item_status': row[3],
                'fk_delivery_type': row[4],
                'unit_price': row[5],
                'tax_amount': row[6],
                'paid_price': row[7],
                'name': row[8],
                'sku': row[9],
                'created_at': row[10],
                'updated_at': row[11],
                'last_status_change': row[12],
                'original_unit_price': row[13],
                'shipping_type': row[14],
                'real_delivery_date': row[15],
                'bob_id_supplier': row[16],
                'is_marketplace': row[17],
            }
            
            if i == 1:  # check if the header values line up
                if not data['id_sales_order_item'] == 'id_sales_order_item':
                    raise InvalidFileException(
                        error_msg.format('id_sales_order_item'))
                if not data['bob_id_sales_order_item'] == \
                        'bob_id_sales_order_item':
                    raise InvalidFileException(
                        error_msg.format('bob_id_sales_order_item'))
                if not data['fk_sales_order'] == 'fk_sales_order':
                    raise InvalidFileException(
                        error_msg.format('fk_sales_order'))
                if not data['fk_sales_order_item_status'] == \
                        'fk_sales_order_item_status':
                    raise InvalidFileException(
                        error_msg.format('fk_sales_order_item_status'))
                if not data['fk_delivery_type'] == 'fk_delivery_type':
                    raise InvalidFileException(
                        error_msg.format('fk_delivery_type'))
                if not data['unit_price'] == 'unit_price':
                    raise InvalidFileException(error_msg.format('unit_price'))
                if not data['tax_amount'] == 'tax_amount':
                    raise InvalidFileException(error_msg.format('tax_amount'))
                if not data['paid_price'] == 'paid_price':
                    raise InvalidFileException(error_msg.format('paid_price'))
                if not data['name'] == 'name':
                    raise InvalidFileException(error_msg.format('name'))
                if not data['sku'] == 'sku':
                    raise InvalidFileException(error_msg.format('sku'))
                if not data['created_at'] == 'created_at':
                    raise InvalidFileException(error_msg.format('created_at'))
                if not data['updated_at'] == 'updated_at':
                    raise InvalidFileException(error_msg.format('updated_at'))
                if not data['last_status_change'] == 'last_status_change':
                    raise InvalidFileException(
                        error_msg.format('last_status_change'))
                if not data['original_unit_price'] == 'original_unit_price':
                    raise InvalidFileException(
                        error_msg.format('original_unit_price'))
                if not data['shipping_type'] == 'shipping_type':
                    raise InvalidFileException(
                        error_msg.format('shipping_type'))
                if not data['real_delivery_date'] == 'real_delivery_date':
                    raise InvalidFileException(
                        error_msg.format('real_delivery_date'))
                if not data['bob_id_supplier'] == 'bob_id_supplier':
                    raise InvalidFileException(
                        error_msg.format('bob_id_supplier'))
                if not data['is_marketplace'] == 'is_marketplace':
                    raise InvalidFileException(
                        error_msg.format('is_marketplace'))
            else:
                process_so_item_data(data=data, db_service=db_service)
        
        print(f'Processed {i} sales order item(s).')


def load_so_item_status_from_file(path, db_service):
    with open(path) as csv_file:
        csv_reader = csv.reader(csv_file)
        error_msg = 'Missing required header: {}'
        
        for i, row in enumerate(csv_reader, 1):
            data = {
                'id_sales_order_item_status': row[0],
                'fk_oms_function': row[1],
                'status': row[2],
                'desc': row[3],
                'deprecated': row[4],
                'updated_at': row[5],
            }
            
            if i == 1:  # check if the header values line up
                if not data['id_sales_order_item_status'] == \
                        'id_sales_order_item_status':
                    raise InvalidFileException(
                        error_msg.format('id_sales_order_item_status'))
                if not data['fk_oms_function'] == 'fk_oms_function':
                    raise InvalidFileException(
                        error_msg.format('fk_oms_function'))
                if not data['status'] == 'status':
                    raise InvalidFileException(error_msg.format('status'))
                if not data['desc'] == 'desc':
                    raise InvalidFileException(error_msg.format('desc'))
                if not data['deprecated'] == 'deprecated':
                    raise InvalidFileException(error_msg.format('deprecated'))
                if not data['updated_at'] == 'updated_at':
                    raise InvalidFileException(error_msg.format('updated_at'))
            else:
                process_so_item_status_data(data=data, db_service=db_service)
        print(f'Processed {i} sales order item status.')


def load_so_item_status_history_from_file(path, db_service):
    with open(path) as csv_file:
        csv_reader = csv.reader(csv_file)
        error_msg = 'Missing required header: {}'
        
        for i, row in enumerate(csv_reader, 1):
            data = {
                'id_sales_order_item_status_history': row[0],
                'fk_sales_order_item': row[1],
                'fk_sales_order_item_status': row[2],
                'created_at': row[3],
            }
            
            if i == 1:  # check if the header values line up
                if not data['id_sales_order_item_status_history'] == \
                        'id_sales_order_item_status_history':
                    raise InvalidFileException(
                        error_msg.format('id_sales_order_item_status_history'))
                if not data['fk_sales_order_item'] == 'fk_sales_order_item':
                    raise InvalidFileException(
                        error_msg.format('fk_sales_order_item'))
                if not data['fk_sales_order_item_status'] == \
                        'fk_sales_order_item_status':
                    raise InvalidFileException(
                        error_msg.format('fk_sales_order_item_status'))
                if not data['created_at'] == 'created_at':
                    raise InvalidFileException(error_msg.format('created_at'))
            else:
                process_so_item_status_history_data(data=data,
                                                    db_service=db_service)
        print(f'Processed {i} sales order item status history.')


def process_so_item_data(data, db_service):
    if data['real_delivery_date'] == 'NULL':
        data['real_delivery_date'] = None
    
    db_service.add_so_item(**data)


def process_so_item_status_data(data, db_service):
    db_service.add_so_item_status(**data)


def process_so_item_status_history_data(data, db_service):
    db_service.add_so_item_status_history(**data)
