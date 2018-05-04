from openpyxl import load_workbook

from core.exceptions import InvalidFileException


def load_analysis_from_file(path, db_service):
    """
    Load analysis data from an existing file and saves it to the database.
    
    Accepts:
        * .XLSX
    """
    
    print(f'Processing "{path}"...')
    wb = load_workbook(filename=path)
    
    load_package_sheet(workbook=wb, db_service=db_service)
    load_region_sheet(workbook=wb, db_service=db_service)
    
    # TODO: do this process while reading the package worksheet
    populate_package_regions(db_service=db_service)


def load_package_sheet(workbook, db_service, sheet_name=None):
    """
    Processes worksheets with the following headers:
    
        * ID
        * Address
        * Major Region
        * package_number
        * shipped at
        * delivered_at
        * leadtime
    """
    
    if not sheet_name:
        sheet_name = 'Package'
    
    sheet = workbook[sheet_name]
    error_msg = 'Missing required header: {}'
    
    for i, row in enumerate(sheet.rows, 1):
        data = {
            'id': row[0].value,
            'address': row[1].value,
            'major_region': row[2].value,
            'package_number': row[3].value,
            'shipped_at': row[4].value,
            'delivered_at': row[5].value,
            'lead_time': row[6].value,
        }
        
        if i == 1:  # check if the header values line up
            if not data['id'] == 'ID':
                raise InvalidFileException(error_msg.format('ID'))
            if not data['address'] == 'Address':
                raise InvalidFileException(error_msg.format('Address'))
            if not data['major_region'] == 'Major Region':
                raise InvalidFileException(error_msg.format('Major Region'))
            if not data['package_number'] == 'package_number':
                raise InvalidFileException(error_msg.format('package_number'))
            if not data['shipped_at'] == 'shipped at':
                raise InvalidFileException(error_msg.format('shipped at'))
            if not data['delivered_at'] == 'delivered_at':
                raise InvalidFileException(error_msg.format('delivered_at'))
            if not data['lead_time'] == 'leadtime':
                raise InvalidFileException(error_msg.format('leadtime'))
        else:
            process_package_data(data=data, db_service=db_service)
    
    print(f'Processed {i} package(s).')


def load_region_sheet(workbook, db_service, sheet_name=None):
    """
    Processes worksheets with the following headers:
    
        * ID
        * Region
        * Major Region
    """
    
    if not sheet_name:
        sheet_name = 'Region'
    
    sheet = workbook[sheet_name]
    error_msg = 'Missing required header: {}'
    
    for i, row in enumerate(sheet.rows, 1):
        data = {
            'id': row[0].value,
            'region': row[1].value,
            'major_region': row[2].value,
        }
        
        if i == 1:  # check if the header values line up
            if not data['id'] == 'ID':
                raise InvalidFileException(error_msg.format('ID'))
            if not data['region'] == 'Region':
                raise InvalidFileException(error_msg.format('Region'))
            if not data['major_region'] == 'Major Region':
                raise InvalidFileException(error_msg.format('Major Region'))
        else:
            process_region_data(data=data, db_service=db_service)
    
    print(f'Processed {i} region(s).')


def process_package_data(data, db_service):
    # populate region
    data['region'] = None
    
    # populate lead_time
    data['lead_time'] = data['delivered_at'] - data['shipped_at']
    
    db_service.add_package(address=data['address'],
                           region=data['region'],
                           package_number=data['package_number'],
                           shipped_at=data['shipped_at'],
                           delivered_at=data['delivered_at'],
                           lead_time=data['lead_time'],
                           id_=data['id'])


def process_region_data(data, db_service):
    db_service.add_region(region=data['region'],
                          major_region=data['major_region'],
                          id_=data['id'])


def populate_package_regions(db_service):
    print('Updating package regions...')
    for region in db_service.get_regions():
        db_service.update_package_addresses(region=region)
