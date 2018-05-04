from sqlalchemy import Column, Integer, String
from sqlalchemy.orm import relationship

from .models import BaseModel


class Region(BaseModel):
    __tablename__ = 'region'
    
    id = Column(Integer, primary_key=True, nullable=False, autoincrement=True)
    region = Column(String(40))
    major_region = Column(String(10))
    
    def serialize(self):
        return {
            'id': self.id,
            'region': self.region,
            'major_region': self.major_region,
        }
