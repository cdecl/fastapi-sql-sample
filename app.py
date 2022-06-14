from typing import Union
from fastapi import FastAPI, Depends
from fastapi.encoders import jsonable_encoder
from datetime import datetime
from pydantic import BaseModel

from sqlalchemy.orm import Session
from database import get_db, engine
import models

app = FastAPI()

# create table : ddl
models.Base.metadata.create_all(bind=engine)

@app.get("/")
def root():
    dt = datetime.now()
    return { "hello" : dt }

class User(BaseModel):
    id: int
    name: str

@app.get("/select")
def select(db: Session = Depends(get_db)):
    cur = db.query(models.User).all()
    return { 'r': cur }

@app.get("/add")
def add(u: User, db: Session = Depends(get_db)):
    try:
        user = jsonable_encoder(u)
        dbuser = models.User(**user)
        db.merge(dbuser)
        db.commit()
    except Exception as e:
        pass
    return { 'r': 'ok', 'd': user}


