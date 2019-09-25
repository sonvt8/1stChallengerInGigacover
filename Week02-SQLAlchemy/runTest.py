from database import Database
from sqlalchemy import create_engine
from sqlalchemy import Column
from sqlalchemy import String, Integer, Date, PrimaryKeyConstraint, ForeignKey
from sqlalchemy.ext.declarative import declarative_base

# Make a connection to database
db = Database()
Base = declarative_base()

# The Python Debugger
# from pdb import  set_trace; set_trace()

# Creat a class Customer
class Customer(Base):

    __tablename__ = 'customers'

    id = Column(Integer, primary_key=True) # Auto-increment should be default autoincrement=True
    name = Column(String)
    birth = Column(Date)
    address = Column(String(50))
    phone = Column(String(20))

    def __init__(self, id, name, birth, address, phone):
        self.id = id
        self.name = name
        self.birth = birth
        self.address = address
        self.phone = phone

# Read
customers = db.session.query(Customer)
for customer in customers:
    sentence = f'{customer.id} | {customer.name} | {customer.birth} | {customer.address} | {customer.phone}'
    print(sentence)

