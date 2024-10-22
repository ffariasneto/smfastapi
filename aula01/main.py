from fastapi import FastAPI

app = FastAPI()

products = [
    {
            "id": 1,
            "name": "Product 1",
            "price": 28.90,
            "stock": 50
        },
        {
            "id": 2,
            "name": "Product 2",
            "price": 23.90,
            "stock": 30
        },
        {
            "id": 3,
            "name": "Product 3",
            "price": 19.90,
            "stock": 100
        }
]

@app.get("/saudacao") # o @ é o decorate permite atribuir uma função a classe
def read_root():
    return {
        "message": "hello world"
    }

@app.get("/lista_produtos")
def read_products():
    return {
        "products": products
    }

@app.get("/qte_produtos")
def quantidade():
    return {
        "products": products,
        "quantidade": len(products)
    }