from flask import render_template

from services.database import db_service


def view_packages():
    context = {}
    context['title'] = 'Packages'
    context['headers'] = ['ID', 'Address', 'Region', 'Package Number',
                          'Shipped At', 'Delivered At', 'Lead Time']
    context['rows'] = db_service.get_packages()
    
    return render_template('analysis/packages.html', context=context)


def view_regions():
    context = {}
    context['title'] = 'Regions'
    context['headers'] = ['ID', 'Region', 'Major Region']
    context['rows'] = db_service.get_regions()
    
    return render_template('analysis/regions.html', context=context)
