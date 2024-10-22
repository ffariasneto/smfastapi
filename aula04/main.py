from fastapi import FastAPI
from routes import products, books

app = FastAPI()

app.include_router(products.router)
app.include_router(books.router)

@app.get("/")
def read_root():
    return {"message": "api running"}