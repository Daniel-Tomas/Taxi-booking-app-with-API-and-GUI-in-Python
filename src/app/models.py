from sqlalchemy import Boolean, Column, ForeignKey, Integer, String, Date, Time
from sqlalchemy.orm import relationship

from .database import Base


class User(Base):
    __tablename__ = "users"

    nickname = Column(String, primary_key=True, unique=True, index=True)
    email = Column(String, index=True)
    pay_method = Column(String)
    phone_number = Column(String)
    password = Column(String)
    is_active = Column(Boolean, default=False)

    requests = relationship("Request", back_populates="user")


class Taxi(Base):
    __tablename__ = "taxies"

    name = Column(String, primary_key=True, index=True)
    is_free = Column(Boolean, default=True)
    actual = Column(String)
    destination = Column(String)

    requests = relationship("Request", back_populates="taxi")


class Request(Base):
    __tablename__ = "requests"

    date = Column(Date, primary_key=True, index=True)
    time = Column(Time, primary_key=True, index=True)
    origin = Column(String)
    destination = Column(String)

    user_nickname = Column(String, ForeignKey("users.nickname"))
    taxi_name = Column(String, ForeignKey("taxies.name"))

    user = relationship("User", back_populates="requests")
    taxi = relationship("Taxi", back_populates="requests")
