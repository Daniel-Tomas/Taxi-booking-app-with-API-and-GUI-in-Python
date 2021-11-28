from sqlalchemy.orm import sessionmaker
from faker import Faker
from app.database import engine
from app.models import *
from datetime import datetime

session = sessionmaker(engine)()
fake = Faker("es_ES")

users = ['julio69', 'XxPacoxX', 'luisito', 'albertoCR7']
taxies = ['taxi_seguro', 'taxi_barato', 'taxi_de_aurelio', 'taxi_tesla']

def reset_all():
    session.query(User).delete()
    session.query(Taxi).delete()
    session.query(Request).delete()
    session.commit()


def create_users():
    for name in users:
        user = User(nickname=name, email=fake.email(), pay_method="tarjeta",
                    phone_number=fake.phone_number(), password=fake.password(), is_active=True)
        session.add(user)

    admin = User(nickname="admin", email=fake.email(), pay_method="tarjeta",
                 phone_number=fake.phone_number(), password='admin', is_active=True)
    session.add(admin)

    session.commit()


def create_taxies():
    for name in taxies:
        taxi = Taxi(name=name, is_free=True,
                    actual="madrid", destination="barcelona")
        session.add(taxi)
    session.commit()


def create_requests():
    for user, taxi in zip(users, taxies):
        request = Request(date=datetime.now().date(), time=datetime.now().time(
        ), origin=fake.address(), destination=fake.address(), user_nickname=user, taxi_name=taxi)
        session.add(request)
    session.commit()


reset_all()
create_users()
create_taxies()
create_requests()
