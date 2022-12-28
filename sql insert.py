from sqlalchemy import*
from sqlalchemy.orm import sessionmaker
from sqlalchemy.ext.declarative import declarative_base

engin=create_engine("mysql+mysqlconnector://root:12345678fgh@localhost:3306/pr",echo=False)

Session=sessionmaker(bind=engin)
session=Session()

base=declarative_base()

class st(base):
    __tablename__="pr1"

    id=Column(Integer,primary_key=True, autoincrement=True)
    name=Column(String(50))
    age=Column(Integer)
    grade=Column(String(50))

base.metadata.create_all(engin)
st1=st(name='mohammadreza',age=14,grade='usa')

session.add(st1)
session.commit()