# Endpoints
São como portas de entrada para uma API, que permitem que outros sistemas ou aplicativos interajam com ela.

Para acessar um endpoint, você envia uma solicitação HTTP para um endereço específico, e a API responde com dados ou comandos específicos.

Cada endpoint é único.

## Endpoints estáticos
São pontos fixo na API, como páginas em uma website.

A URL do endpoint é fixa e sempre aponta para a mesma função.

## Endpoints dinâmicos
Permitem flexibilidade na interação com sua API

## Path Parameters
São variáveis que você insere diretamente na URL do endpoint, geralmente para identificar um recurso específico.

## Query Parameters
São usados para filtrar, ordenar ou refinar os dados que está sendo recuperado no endpoint.

## Boas práticas com endpoints

- Uso correto de métodos HTTP: usar os vervos de acordo com a função de cada um.
- Path Parameters vs Query Parameters: usar o path para recursos específicos e o query para filtros e consultas menos específicas.
- Estrutura de Rotas Simples e Consistentes: manter as rotas curtas e simples.

```
from fastapi import FastAPI

app = FastAPI()

products = [
    {
        "product_id": 1,
        "name": "Queijo",
        "price": 2.0
    },
    {
        "product_id": 2,
        "name": "Maçã",
        "price": 2.5
    },
    {
        "product_id": 3,
        "name": "Pera",
        "price": 10
    }
]

@app.get('/products')
def get_products(min_price: float = None, max_price: float = None, name: str = None):
    filt_products = products

    if min_price:
        filt_products = [product for product in filt_products if product["price"] >= min_price]
    
    if max_price:
        filt_products = [product for product in filt_products if product["price"] <= max_price]
    
    if name:
        filt_products = [product for product in filt_products if name.lower() in product["name"].lower()]

    return {
        "products": filt_products
        }
    
@app.get('/products/{product_id}')
def get_product(product_id: int):
    for product in products:
        if product_id == product['product_id']:
            return {
                "product": product
            }
    return {
        "message": "Not found"
    }
    ```