from sqlalchemy import  Column, Integer, String, Float, Enum, DateTime, func
from .database import Base
from enum import Enum as Pyenum

class UserType(Pyenum):
    ADMIN = 'admin'
    USER = 'user'
    STUDENT = 'student'
    EMPLOYEE = 'employee'
    MANAGER = 'manager'

class User(Base):
    __tablename__ = 'user'
    
    id = Column(Integer, primary_key=True, index=True)
    name = Column(String(255), index=True)
    email = Column(String(255), unique=True, index=True)
    hashed_password = Column(String(255))
    type = Column(Enum(UserType, name='user_type'), nullable=False)
    created_at = Column(DateTime(timezone=True), server_default=func.now())
    updated_at = Column(DateTime(timezone=True), onupdate=func.now(), server_default=func.now())
    
    