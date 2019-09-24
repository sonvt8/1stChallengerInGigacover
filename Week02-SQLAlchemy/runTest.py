from database import Database
from sqlalchemy import create_engine
from sqlalchemy import Column
from sqlalchemy import String, Integer, Date, PrimaryKeyConstraint, ForeignKey
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import sessionmaker

db = Database()

# The Python Debugger
# from pdb import  set_trace; set_trace()

session = sessionmaker(bind = Database.engine)()

Base = declarative_base()

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
customers = session.query(Customer)
for customer in customers:
    print(str(customer.id) + ' | ' + customer.name +  ' |  ' + str(customer.birth) +  ' |  ' + customer.address
          + ' |  ' + customer.phone)