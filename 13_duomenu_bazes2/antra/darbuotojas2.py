from sqlalchemy import *
from sqlalchemy.ext.declarative import declarative_base
from datetime import datetime

engine = create_engine("sqlite:///darbuotojas.db")
Base = declarative_base()

class Darbuotojas(Base):
    __tablename__ = "Darbuotojas"

    id = Column(Integer, primary_key=True)
    name = Column("Name", String)
    surname = Column("Surname", String)
    birth_date = Column("Date of birth", String)
    position = Column("Position", String)
    salary = Column("Salary", Integer)
    start_date = Column("Start Date", String, default=datetime.utcnow)

    def __init__(self, name, surname, birth_date, position, salary, start_date):
        self.name = name
        self.surname = surname
        self.birth_date = birth_date
        self.position = position
        self.salary = salary
        self.start_date = start_date




    def __str__(self):
        return f"{self.name}, {self.surname}, {self.birth_date}, {self.position}, {self.salary}, {self.start_date}"

Base.metadata.create_all(engine)
