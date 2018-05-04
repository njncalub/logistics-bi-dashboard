from sqlalchemy import Column, DateTime, ForeignKey, Integer, Interval, String
from sqlalchemy.orm import relationship

from .models import BaseModel


class Package(BaseModel):
    __tablename__ = 'package'
    
    id = Column(Integer, primary_key=True, nullable=False, autoincrement=True)
    address = Column(String(100))
    region_id = Column(Integer, ForeignKey('region.id',
                                           ondelete='CASCADE'))
    region = relationship('Region', backref='packages')
    package_number = Column(String(20))
    shipped_at = Column(DateTime)
    delivered_at = Column(DateTime)
    lead_time = Column(Interval)
    
    def serialize(self):
        return {
            'id': self.id,
            'address': self.address,
            'region': self.region.id,
            'package_number': self.package_number,
            'shipped_at': self.shipped_at,
            'delivered_at': self.delivered_at,
            'lead_time': self.lead_time,
        }
