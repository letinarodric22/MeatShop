# database.py
from sqlalchemy import create_engine, Column, Integer, String, DateTime
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import sessionmaker
from datetime import datetime

# Database credentials
username = 'postgres'
password = '1234'
host = 'localhost'
port = '5432'
database = 'meatshop'

# Create an engine
engine = create_engine(f'postgresql+psycopg2://{username}:{password}@{host}:{port}/{database}')

Base = declarative_base()

class MeatProduct(Base):
    __tablename__ = 'meat_products'
    id = Column(Integer, primary_key=True)
    name = Column(String, nullable=False)
    price = Column(Integer, nullable=False)
    buying_price = Column(Integer, nullable=False)
    selling_price = Column(Integer, nullable=False)
    created_at = Column(DateTime, default=datetime.utcnow, nullable=False)

# Initialize the session
Session = sessionmaker(bind=engine)
session = Session()

def drop_and_recreate():
    Base.metadata.drop_all(engine)
    Base.metadata.create_all(engine)
