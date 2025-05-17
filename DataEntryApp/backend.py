from fastapi import FastAPI
from sqlalchemy.orm import sessionmaker
from models import training_data, engine
from schemas import *


Session = sessionmaker(bind=engine)

session = Session()

app = FastAPI()

@app.get("/")
async def root():
    return {"Message": "Hello world "}

@app.post("/new_msg")
async def new_msg(User: Schema_User):
    User_Msg = User.model_dump()

    New_User_Msg = training_data(user=User_Msg["user"])
    session.add(New_User_Msg)
    session.commit()

    return {"message": "New message added correctly"}


@app.get("/all_msg")
async def all_msg():
    tData = session.query(training_data).all()

    return tData

@app.patch("/answer_msg")
async def answer_msg(response: Schema_Response):
    Response = response.model_dump()
    msg = session.query(training_data).filter_by(id=Response["id"]).one_or_none()

    if msg == None:
        return "No message found"
    else:
        msg.agent = Response["agent"]

    session.commit()

    return session.query(training_data).filter_by(id=Response["id"]).one_or_none()