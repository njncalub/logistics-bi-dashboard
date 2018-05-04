from openpyxl import load_workbook

from core.exceptions import InvalidFileException


def load_analysis_from_file(path):
    """
    Load analysis data from an existing file and saves it to the database.
    
    Accepts:
        * .XLSX
    """
    
    wb = load_workbook(filename=path)
    
    load_region_sheet(workbook=wb)
    load_package_sheet(workbook=wb)


def load_region_sheet(workbook, sheet_name=None):
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
    
    for i, row in enumerate(sheet.rows):
        data = {
            'id': row[0].value,
            'region': row[1].value,
            'major_region': row[2].value,
        }
        
        if i == 0:  # check if the header values line up
            if not data['id'] == 'ID':
                raise InvalidFileException(error_msg.format('ID'))
            if not data['region'] == 'Region':
                raise InvalidFileException(error_msg.format('Region'))
            if not data['major_region'] == 'Major Region':
                raise InvalidFileException(error_msg.format('Major Region'))
        else:
            process_region_data(data=data)


def process_region_data(data):
    print(data)


def load_package_sheet(workbook, sheet_name=None):
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
    
    for i, row in enumerate(sheet.rows):
        data = {
            'id': row[0].value,
            'address': row[1].value,
            'major_region': row[2].value,
            'package_number': row[3].value,
            'shipped_at': row[4].value,
            'delivered_at': row[5].value,
            'lead_time': row[6].value,
        }
        
        if i == 0:  # check if the header values line up
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
            process_package_data(data=data)


def process_package_data(data):
    print(data)
