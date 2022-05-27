from sqlalchemy import *
from sqlalchemy.ext.declarative import declarative_base

engine = create_engine("sqlite:///darbuotojai.db")
Base = declarative_base()

class Darbuotojai(Base):
    __tablename__ = "Darbuotojai"

    id = Column(Integer, primary_key=True)
    vardas = Column("Vardas", String)
    pavarde = Column("Pavarde", String)
    atlyginimas = Column("Atlyginimas", Integer)


    def __init__(self, vardas, pavarde, atlyginimas):
        self.vardas = vardas
        self.pavarde = pavarde
        self.atlyginimas = atlyginimas

    def __str__(self):
        return f"{self.vardas}, {self.pavarde}, {self.atlyginimas}"

Base.metadata.create_all(engine)