import time
from fastapi import FastAPI, Request
from database import create_table
from routes import users, calls
from middlewares import create_token, auth


app = FastAPI()

app.include_router(users.router)
app.include_router(calls.router)

@app.middleware("http")
def log(request: Request, call_next):
    start_time = time.time()
    print(f"Requisição recebida: {request.url}")

    response = call_next(request)

    process_time = time.time() - start_time
    print(f"Tempo de processamento: {process_time}")
    return response

@app.middleware("http")
def validate_token(request: Request, call_next):
    return auth(request, call_next)


@app.on_event("startup")
def on_startup():
    create_table()

@app.get("/")
def read_api():
    dados = {
         "email": "francisco.fariasneto14@gmail.com"
         }
    token = create_token(dados)
    return {"token": token}

@app.get("/")
def read_api():
    return {'message': "hello world"}