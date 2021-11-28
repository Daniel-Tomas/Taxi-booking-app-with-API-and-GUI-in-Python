from typing import List, Optional
from pydantic import BaseModel
from datetime import date, time


class RequestBase(BaseModel):
    date: date
    time: time
    origin: str
    destination: str


class RequestCreate(RequestBase):
    pass


class Request(RequestBase):
    taxi_name: str
    user_nickname: str

    class Config:
        orm_mode = True


class UserBase(BaseModel):
    nickname: str
    email: str
    pay_method: str
    phone_number: str


class UserCreate(UserBase):
    password: str


class User(UserBase):
    is_active: bool
    # requests: List[Request] = []w

    class Config:
        orm_mode = True


class Login(BaseModel):
    password: str


class TaxiBase(BaseModel):
    name: str
    is_free: bool
    actual: str
    destination: str


class TaxiCreate(TaxiBase):
    pass


class Taxi(TaxiBase):
    #requests: List[Request] = []

    class Config:
        orm_mode = True
