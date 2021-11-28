from sqlalchemy.orm import Session
from . import models, schemas
from datetime import date


def create_user(db: Session, user: schemas.UserCreate):
    db_user = models.User(**user.dict())
    db.add(db_user)
    db.commit()
    db.refresh(db_user)
    return db_user


def get_user(db: Session, user_nickname: str):
    return db.query(models.User).filter(models.User.nickname == user_nickname).first()


def login(db: Session, login: schemas.Login, user_nickname: str) -> bool:
    return db.query(models.User).filter(models.User.nickname == user_nickname).filter(
        models.User.password == login.password).filter(models.User.is_active == True).first()


def update_validation(db: Session, user_nickname: str):
    db.query(models.User).filter(models.User.nickname ==
                                 user_nickname).update({models.User.is_active: True})
    db.commit()


def create_taxi(db: Session, taxi: schemas.TaxiCreate):
    db_taxi = models.Taxi(**taxi.dict())
    db.add(db_taxi)
    db.commit()
    db.refresh(db_taxi)
    return db_taxi


def get_taxi(db: Session, taxi_name: str):
    return db.query(models.Taxi).filter(models.Taxi.name == taxi_name).first()


def get_taxies(db: Session, skip: int = 0, limit: int = 100):
    return db.query(models.Taxi).offset(skip).limit(limit).all()


def get_free_taxies(db: Session):
    return db.query(models.Taxi).filter(models.Taxi.is_free == True).all()


def update_taxi_status(db: Session, taxi_name: str, status: bool):
    db.query(models.Taxi).filter(models.Taxi.name ==
                                 taxi_name).update({models.Taxi.is_free: status})
    db.commit()


def create_request(db: Session, request: schemas.RequestCreate, user_nickname: str, taxi_name: str):
    db_request = models.Request(
        **request.dict(), user_nickname=user_nickname, taxi_name=taxi_name)
    db.add(db_request)
    db.commit()
    db.refresh(db_request)
    return db_request


def get_requests(db: Session, date: date):
    return db.query(models.Request).filter(models.Request.date <= date).order_by(models.Request.date).all()
