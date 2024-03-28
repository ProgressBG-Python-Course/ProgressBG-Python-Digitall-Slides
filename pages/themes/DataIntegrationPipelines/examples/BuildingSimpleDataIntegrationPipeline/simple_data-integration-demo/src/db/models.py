from sqlalchemy import create_engine, Column, Integer, String, Date, Numeric, ForeignKey
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import sessionmaker

Base = declarative_base()

class Campaign(Base):
    __tablename__ = 'campaigns'
    campaign_id = Column(Integer, primary_key=True)
    campaign_name = Column(String)

class CRMData(Base):
    __tablename__ = 'crm_data'
    order_id = Column(Integer, primary_key=True)
    customer_id = Column(Integer)
    customer_name = Column(String)
    order_date = Column(Date)
    order_amount = Column(Numeric(10, 2))
    campaign_id = Column(Integer, ForeignKey('campaigns.campaign_id'))
