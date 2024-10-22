from fastapi import FastAPI

app = FastAPI()

employees = [
    {"employee_id": 1, "name": "Francisco", "position": "Manager", "salary": 9500.00},
    {"employee_id": 2, "name": "Fabíola", "position": "Lawyer", "salary": 8000.00},
    {"employee_id": 3, "name": "Bernardo", "position": "RH", "salary": 6000.00},
]

@app.get('/employees/{employee_id}')
def get_employee(employee_id: int):
    for employee in employees:
        if employee_id == employee["employee_id"]:
            return {
                "employee": employee
            }
    return {
        "message": "Not found"
    }

leave_requests = [
    {
        "request_id": 1,
        "employee_id": 1,
        "start_date": "2024-01-15",
        "end_date": "2024-01-20",
        "status": "approved",
        "duration_days": 5
    },
    {
        "request_id": 2,
        "employee_id": 2,
        "start_date": "2024-02-10",
        "end_date": "2024-02-15",
        "status": "approved",
        "duration_days": 5
    },
    {
        "request_id": 3,
        "employee_id": 3,
        "start_date": "2024-03-01",
        "end_date": "2024-03-10",
        "status": "approved",
        "duration_days": 5
    }
]

@app.get('/leave_requests/{request_id}')
def get_leave_requests(request_id: int):
    for leave in leave_requests:
        if request_id == leave["request_id"]:
            return {
                "leave": leave
            }
    return {
        "message": "Not found"
    }

@app.get('/vacations')
def get_vacations(status: str = None, min_duration: int = None, max_duration: int = None):
    vacations = leave_requests

    if status:
        vacations = [vacation for vacation in vacations if status == vacation["status"]]
    
    if max_duration:
        vacations = [vacation for vacation in vacations if vacation["duration_days"] <= max_duration]
    
    if min_duration:
        vacations = [vacation for vacation in vacations if vacation["duration_days"] >= min_duration]

    return {
        "requests": vacations
    }


# products = [
#     {
#         "product_id": 1,
#         "name": "Queijo",
#         "price": 2.0
#     },
#     {
#         "product_id": 2,
#         "name": "Maçã",
#         "price": 2.5
#     },
#     {
#         "product_id": 3,
#         "name": "Pera",
#         "price": 10
#     }
# ]

# @app.get('/products')
# def get_products(min_price: float = None, max_price: float = None, name: str = None):
#     filt_products = products

#     if min_price:
#         filt_products = [product for product in filt_products if product["price"] >= min_price]
    
#     if max_price:
#         filt_products = [product for product in filt_products if product["price"] <= max_price]
    
#     if name:
#         filt_products = [product for product in filt_products if name.lower() in product["name"].lower()]

#     return {
#         "products": filt_products
#         }
    
# @app.get('/products/{product_id}')
# def get_product(product_id: int):
#     for product in products:
#         if product_id == product['product_id']:
#             return {
#                 "product": product
#             }
#     return {
#         "message": "Not found"
#     }