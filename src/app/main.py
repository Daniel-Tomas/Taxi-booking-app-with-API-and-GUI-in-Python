from datetime import datetime, date
from fastapi import FastAPI, BackgroundTasks, Depends, FastAPI, HTTPException, Response
from fastapi.param_functions import Query
from fastapi.responses import HTMLResponse

from sqlalchemy.orm import Session
from typing import List, Optional

from sqlalchemy.sql.sqltypes import Date

from . import crud, models, schemas
from .database import SessionLocal, engine

import smtplib
import ssl
import json
from email.mime.text import MIMEText
from email.mime.multipart import MIMEMultipart

import random

with open('config.json') as config_file:
    config = json.load(config_file)

models.Base.metadata.create_all(bind=engine)

app = FastAPI()


def get_db():
    db = SessionLocal()
    try:
        yield db
    finally:
        db.close()


@app.post("/users/", status_code=201, response_model=schemas.User)
async def create_user(user: schemas.UserCreate, background_tasks: BackgroundTasks, db: Session = Depends(get_db)):
    db_user = crud.get_user(db, user.nickname)
    if db_user:
        raise HTTPException(status_code=400, detail="User existed")
    db_user = crud.create_user(db, user)
    background_tasks.add_task(send_notification, user.email, user.nickname)
    return db_user


@app.get("/users/{user_nickname}", response_model=schemas.User)
async def get_user(user_nickname: str, db: Session = Depends(get_db)):
    db_user = crud.get_user(db, user_nickname)
    if db_user is None:
        raise HTTPException(status_code=404, detail="User not found")
    return db_user


@app.get("/taxies/", response_model=List[schemas.Taxi])
async def get_taxies(skip: int = 0, limit: int = 100, db: Session = Depends(get_db)):
    return crud.get_taxies(db, skip=skip, limit=limit)


@app.get("/taxies/{taxi_name}", response_model=schemas.Taxi)
async def get_taxi(taxi_name: str, db: Session = Depends(get_db)):
    db_taxi = crud.get_taxi(db, taxi_name)
    if db_taxi is None:
        raise HTTPException(status_code=404, detail="Taxi not found")
    return db_taxi


def send_req_to_admin(taxi_name: str) -> str:
    import socket
    HOST = '127.0.0.1'  # The server's hostname or IP address
    PORT = 8080  # The port used by the server

    with socket.socket(socket.AF_INET, socket.SOCK_STREAM) as s:
        s.connect((HOST, PORT))
        print('connected')
        s.sendall(f'{taxi_name}'.encode())
        print('sended')
        data = s.recv(1024)

    print('Received', repr(data))
    return data


@app.post("/users/{user_nickname}/requests", status_code=201, response_model=schemas.Request)
async def create_request(user_nickname: str, request: schemas.RequestCreate, db: Session = Depends(get_db)):
    db_taxies = crud.get_free_taxies(db)
    if db_taxies == []:
        raise HTTPException(status_code=503, detail="No free taxies")

    db_taxi = random.choice(db_taxies)
    taxi_name = db_taxi.name

    resp = send_req_to_admin(taxi_name)
    if resp == b'False':
        raise HTTPException(status_code=403, detail="Request declined")

    crud.update_taxi_status(db, taxi_name, False)
    return crud.create_request(db, request, user_nickname, taxi_name)


@app.get("/users/{user_nickname}/validation", response_class=HTMLResponse)
async def update_validation(user_nickname: str, db: Session = Depends(get_db)):
    crud.update_validation(db, user_nickname)
    return """
    <html>
        <head>
            <title>¡Enhorabuena!</title>
        </head>
        <body>
            <h1>Ha sido activado correctamente tu cuenta</h1>
        </body>
    </html>
    """


@app.post("/users/{user_nickname}/login")
async def login(user_nickname: str, login: schemas.Login, db: Session = Depends(get_db)):
    db_user = crud.get_user(db, user_nickname)
    if db_user is None:
        raise HTTPException(status_code=404, detail="User not found")

    if crud.login(db, login, user_nickname) is None:
        raise HTTPException(
            status_code=401, detail="Incorrect password")

    return Response(status_code=200)


@app.get("/requests/", response_model=List[schemas.Request])
async def get_requests(date: Optional[date] = Query(datetime.now().date()), db: Session = Depends(get_db)):
    return crud.get_requests(db, date=date)


def send_notification(email: str, user_nickname: str):
    context = ssl.create_default_context()

    message = MIMEMultipart("alternative")
    message["Subject"] = "Taxi-app: valida tu cuenta"
    message["From"] = "norply@taxi-app.com"
    message["To"] = email

    html = """\
    <html>
    <body>
        <h2>Bienvenido a Taxi-app</h2>
        <p>Usa este <a href="http://localhost:8000/users/{nickname}/validation">link</a> para validar tu cuenta</p>
    </body>
    </html>
    """.format(nickname=user_nickname)

    message.attach(MIMEText(html, "html"))

    with smtplib.SMTP_SSL("smtp.gmail.com", 465, context=context) as server:
        server.login(config['email']['address'], config['email']['password'])
        server.sendmail("norply@taxi-app.com",
                        email, message.as_string())
