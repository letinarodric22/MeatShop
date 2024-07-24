from sqlalchemy import create_engine, Column, Integer, String
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import sessionmaker

# Database credentials
username = 'postgres'
password = '1234'
host = 'localhost'  # Replace with the appropriate host
port = '5432'  # Default PostgreSQL port
database = 'meatshop'

# Create an engine
engine = create_engine(f'postgresql+psycopg2://{username}:{password}@{host}:{port}/{database}')

Base = declarative_base()

class MeatProduct(Base):
    __tablename__ = 'meat_products'
    id = Column(Integer, primary_key=True)
    name = Column(String)
    price = Column(Integer)

Base.metadata.create_all(engine)

Session = sessionmaker(bind=engine)
session = Session()

# Add a new meat product
new_product = MeatProduct(name='Beef Steak ', price=1500)
session.add(new_product)
session.commit()

# Query all meat products
products = session.query(MeatProduct).all()
for product in products:
    print(product.name, product.price)
