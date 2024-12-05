from sqlalchemy import (
    Column,
    Integer,
    DateTime,
    ForeignKey,
    Text,
    String
)

from datetime import datetime
from db.engine import engine, Base


class Department(Base):
    __tablename__ = "department"
    department_id = Column(Integer, autoincrement=True, primary_key=True)
    department_name = Column(Text, nullable=False)
    department_created_at = Column(DateTime, default=datetime.utcnow)
