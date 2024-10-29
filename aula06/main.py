from fastapi import FastAPI
from database import create_table
from routes import users, calls


app = FastAPI()

app.include_router(users.router)
app.include_router(calls.router)

@app.on_event("startup")
def on_startup():
    create_table()

@app.get("/")
def read_api():
    return {"message": "api running"}