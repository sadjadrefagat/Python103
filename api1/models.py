from sqlalchemy import Column, Integer, Float, String
from database import Base


class Student(Base):
    __tablename__ = "Student"

    StdNo = Column(String, primary_key=True, index=True)
    FirstName = Column(String, nullable=False)
    LastName = Column(String, nullable=False)
    FatherName = Column(String, nullable=True)
    BirthDate = Column(String, nullable=True)
    Average = Column(Float, nullable=True)
    Gender = Column(Integer, nullable=True)
    CityID = Column(Integer, nullable=False)
