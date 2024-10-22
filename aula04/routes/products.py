from fastapi import APIRouter, HTTPException
from schemas.product import Product

products = []

router = APIRouter()

@router.get("/products")
def get_products():
    return products

@router.get("/products/{product_id}")
def get_prodcut(product_id: int):
    for product in products:
        if product_id == product["id"]:
            return product
        
    raise HTTPException(status_code=404, detail="Product not found!")

@router.post("/products")
def create_product(product: Product):
    new_product = {
        "id": len(products) + 1,
        "name": product.name,
        "description": product.description,
        "price": product.price,
        "stock": product.stock
    }

    products.append(new_product)
    return {
        "message": "Product Created",
        "products": products
    }

@router.put("/products/{product_id}")
def update_product(product_id: int, upd_product: Product):
    for product in products:
        if product_id == product["id"]:
            product["name"] = upd_product.name
            product["description"] = upd_product.description
            product["price"] = upd_product.price
            product["stock"] = upd_product.stock

            return {
                "message": "Product updated!",
                "product": product
            }
    raise HTTPException(status_code=404, detail="Product not found!")

@router.delete("/products/{product_id}")
def delete_product(product_id: int):
    for product in products:
        if product_id == product["id"]:
            products.remove(product)

            return {
                "message": "Product deleted"
            }
    raise HTTPException(status_code=404, detail="Product not found")