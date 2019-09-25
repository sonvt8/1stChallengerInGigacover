from database import Database
from sqlalchemy import *
from sqlalchemy.ext.declarative import declarative_base

# Make a connection to database
db = Database()
Base = declarative_base()

# The Python Debugger
# from pdb import  set_trace; set_trace()

# Creat a class Customer
class Customer(Base):

    __tablename__ = 'customers'

    #TODO Son do'ng thang hang` dau' =
    id = Column(Integer, primary_key=True) # Auto-increment should be default autoincrement=True
    name = Column(String)
    birth = Column(Date)
    address = Column(String(50))
    phone = Column(String(20))

    def __init__(self, name, birth, address, phone):
        self.name = name
        self.birth = birth
        self.address = address
        self.phone = phone

#CRUD WITH SQLAlchemy

# CREATE
newCustomer = Customer ('Vũ Thái Bình','19930713','Sài Gòn','0903025581')
db.session.add(newCustomer)
db.session.commit()

# READ
customers = db.session.query(Customer)
for customer in customers:
    sentence = f'{customer.id} | {customer.name} | {customer.birth} | {customer.address} | {customer.phone}'
    print(sentence)

# UPDATE
customer_info = db.session.query(Customer).get(3) # Querry info of customer having ID = 3 #TODO Son typo querry
customer_info.address = 'Vũng Tàu'
customer_info.name = 'Cao Thanh Trúc'
db.session.commit()

# DELETE
customer_info = db.session.query(Customer).get(4)
db.session.delete(customer_info)
db.session.commit()

#TODO Son cuoi' tep chi co' 1 dong tra'ng



