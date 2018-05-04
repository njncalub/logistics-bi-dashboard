from sqlalchemy import (
    Column, DateTime, ForeignKey, Float, Integer, Interval, String,
)
from sqlalchemy.orm import relationship

from .models import BaseModel


class Item(BaseModel):
    __tablename__ = 'ims_sales_order_item'
    
    id_sales_order_item = Column(Integer, primary_key=True, nullable=False,
                                 autoincrement=True)
    bob_id_sales_order_item = Column(Integer)
    fk_sales_order = Column(Integer)
    fk_sales_order_item_status = Column(Integer,
        ForeignKey('ims_sales_order_item_status.id_sales_order_item_status',
                   ondelete='CASCADE'))
    fk_delivery_type = Column(Integer)
    unit_price = Column(Float)
    tax_amount = Column(Integer)
    paid_price = Column(Float)
    name = Column(String(100))
    sku = Column(String(30))
    created_at = Column(DateTime)
    updated_at = Column(DateTime)
    last_status_change = Column(DateTime)
    original_unit_price = Column(Float)
    shipping_type = Column(String(20))
    real_delivery_date = Column(DateTime, nullable=True)
    bob_id_supplier = Column(Integer)
    is_marketplace = Column(Integer)
    
    # relationships
    sales_order_item_status = relationship('ItemStatus',
                                            backref='history_items')
    
    def serialize(self):
        return {
            'id_sales_order_item': self.id_sales_order_item,
            'bob_id_sales_order_item': self.bob_id_sales_order_item,
            'fk_sales_order': self.fk_sales_order,
            'fk_sales_order_item_status': self.fk_sales_order_item_status,
            'fk_delivery_type': self.fk_delivery_type,
            'unit_price': self.unit_price,
            'tax_amount': self.tax_amount,
            'paid_price': self.paid_price,
            'name': self.name,
            'sku': self.sku,
            'created_at': self.created_at,
            'updated_at': self.updated_at,
            'last_status_change': self.last_status_change,
            'original_unit_price': self.original_unit_price,
            'shipping_type': self.shipping_type,
            'real_delivery_date': self.real_delivery_date,
            'bob_id_supplier': self.bob_id_supplier,
            'is_marketplace': self.is_marketplace,
        }


class ItemStatus(BaseModel):
    __tablename__ = 'ims_sales_order_item_status'
    
    id_sales_order_item_status = Column(Integer, primary_key=True,
                                        nullable=False, autoincrement=True)
    fk_oms_function = Column(Integer)
    status = Column(String(35))
    desc = Column(String(150))
    deprecated = Column(Integer)
    updated_at = Column(DateTime)
    
    def serialize(self):
        return {
            'id_sales_order_item_status': self.id_sales_order_item_status,
            'fk_oms_function': self.fk_oms_function,
            'status': self.status,
            'desc': self.desc,
            'deprecated': self.deprecated,
            'updated_at': self.updated_at,
        }


class ItemStatusHistory(BaseModel):
    __tablename__ = 'ims_sales_order_item_status_history'
    id_sales_order_item_status_history = Column(Integer, primary_key=True,
                                                nullable=False,
                                                autoincrement=True)
    fk_sales_order_item = Column(Integer, ForeignKey(
        'ims_sales_order_item.id_sales_order_item', ondelete='CASCADE'))
    fk_sales_order_item_status = Column(Integer, ForeignKey(
        'ims_sales_order_item_status.id_sales_order_item_status',
        ondelete='CASCADE'))
    created_at = Column(DateTime)
    
    # relationships
    sales_order_item = relationship('Item', backref='status_history')
    sales_order_item_status = relationship('ItemStatus', backref='history')
    
    def serialize(self):
        return {
            'id_sales_order_item_status_history': \
                self.id_sales_order_item_status_history,
            'fk_sales_order_item': self.fk_sales_order_item,
            'fk_sales_order_item_status': self.fk_sales_order_item_status,
            'created_at': self.created_at,
        }
