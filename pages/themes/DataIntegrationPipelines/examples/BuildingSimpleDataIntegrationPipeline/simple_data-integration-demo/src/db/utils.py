# db_utils.py
from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker
from src.db.models import Base

DATABASE_URL = "sqlite:///crm_data.db"

def init_db():
    engine = create_engine(DATABASE_URL, echo=True)

    # Create database tables
    Base.metadata.create_all(engine)
    return engine

def get_session(engine):
    Session = sessionmaker(bind=engine)
    return Session()