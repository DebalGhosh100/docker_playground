from sqlalchemy import Column, Integer, DateTime, ForeignKey, Text, String
from datetime import datetime
from db.engine import engine, Base


class Employee(Base):
    __tablename__ = "employee"
    employee_id = Column(Integer, primary_key=True, autoincrement=True)
    employee_name = Column(Text, nullable=False)
    employee_numer = Column(Text, nullable=False, unique=True)
    employee_age = Column(Integer, nullable=False)
    employee_created_at = Column(DateTime, default=datetime.utcnow)
    employee_department_id = Column(
        Integer, ForeignKey("department.department_id"))
