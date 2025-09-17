"""
    Model for database
"""

from sqlalchemy import Column, Integer, String
from sqlalchemy.ext.declarative import declarative_base

Base = declarative_base()

class Patient(Base):
    __tablename__ = 'patients'
    
    id = Column(Integer, primary_key=True)
    name = Column(String(100), nullable=False)
    age = Column(Integer, nullable=False)
    disease = Column(String(100), nullable=False)

    def __repr__(self):
        return f"<Patient(id={self.id}, name={self.name}, age={self.age}, disease={self.disease})>"
