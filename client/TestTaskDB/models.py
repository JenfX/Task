from core.db import Base
from sqlalchemy import Column, Integer, VARCHAR

class EnteredNumbers(Base):
    __tablename__ = "enterednumbers"
    id = Column(Integer, primary_key=True, index=True, unique=True)
    number = Column(Integer)

class PrimeFactors(Base):
    __tablename__ = "primefactors"
    id = Column(Integer, primary_key=True, index=True, unique=True)
    prfactors = Column(VARCHAR(50))