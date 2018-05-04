from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker

from .utils import destroy_database, initialize_database
from .models import Package, Region


class DataService(object):
    """
    Service for handling the database connection.
    """
    
    def __init__(self, engine):
        if not engine:
            raise ValueError('The values specified in engine parameter has ' \
                             'to be supported by SQLAlchemy.')
        
        self.engine = engine
        db_engine = create_engine(engine)
        db_session = sessionmaker(bind=db_engine)
        self.session = db_session()
    
    def init_database(self):
        initialize_database(engine=self.engine)
    
    def drop_database(self):
        destroy_database(engine=self.engine)
    
    def add_region(self, region, major_region, id_=None):
        """
        Creates and saves a new Region to the database.
        
        :param id_: Existing id of the region
        :param region: Name of the region
        :param major_region: Name of the Major Region
        """
        new_region = Region(id=id_,
                            region=region,
                            major_region=major_region)
        self.session.add(new_region)
        self.session.commit()
        
        return new_region
    
    def get_regions(self, region=None):
        if region:
            found = self.session.query(Region).filter(Region.region == region)
        else:
            found = self.session.query(Region).all()
        
        return found
    
    def update_package_addresses(self, region):
        """
        Find package by sub region name.
        
        TODO: update this to not resort to using this hack.
        """
        
        found_packages = self.session.query(Package).filter(
            Package.address.startswith(region.region))
        
        if not found_packages:
            return
        
        for package in found_packages:
            package.region = region
            
            self.session.add(package)
            self.session.commit()
    
    def add_package(self, address, region, package_number, shipped_at,
                    delivered_at, lead_time=None, id_=None):
        """
        Creates and saves a new Package to the database.
        
        :param id_: Existing id of the package
        :param address: The address of the recipient
        :param region: FK of the region
        :param package_number: Unique package number
        :param shipped_at: The time when the package is shipped
        :param delivered_at: The time when the package is delivered to customer
        :param lead_time: The time from when the package is shipped
            until it is delievered to customer
        """
        new_package = Package(id=id_,
                              address=address,
                              region=region,
                              package_number=package_number,
                              shipped_at=shipped_at,
                              delivered_at=delivered_at,
                              lead_time=lead_time)
        self.session.add(new_package)
        self.session.commit()
        
        return new_package
