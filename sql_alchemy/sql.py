from unittest import result
from sqlalchemy import Column, Float, create_engine, Integer, String
from sqlalchemy.orm import sessionmaker

engine = create_engine('sqlite:///furniture.db', echo = True)
from sqlalchemy.ext.declarative import declarative_base
Base = declarative_base()

class Computer(Base):
    __tablename__ = 'computer'

    id = Column(Integer, primary_key = True)
    year = Column(String)
    price = Column(Float)
    owner = Column(String)

Base.metadata.create_all(engine)

#Create session
Session = sessionmaker(bind = engine)
session = Session()


# Commit/ Insert records cho Computer
session.add_all([Computer(id = 1000, year = 2018, price = 18,owner = 'An'),
                 Computer(id = 2000, year = 2022, price = 35,owner = 'Kiki'),
                 Computer(id = 3000, year = 2021, price = 55,owner = 'HQJ'),
                 Computer(id = 4000, year = 2020, price = 77,owner = 'DM')])

session.commit()

# Query Computer
result = session.query(Computer).all()

for row in result:
    print("ID:", row.id, "year",row.year, "price:",row.price, "owner:",row.owner)

#Delete Computer
result = Computer.query.filter(Computer.id == 4000).delete()
session.commit()