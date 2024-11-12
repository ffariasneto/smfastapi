from fastapi.testclient import TestClient
from main import app
# from middlewares import create_token, auth

client = TestClient(app)

headers = {"Authorization": "eyJhbGciOiJIUzI1NiIsInR5cCI6IkpXVCJ9.eyJlbWFpbCI6ImZyYW5jaXNjby5mYXJpYXNuZXRvMTRAZ21haWwuY29tIn0._32Li2OYF1gcIcAu0Ra0KC3tzPJ-JwykhJOw1Mj-fZc"}

 

# def get_auth_token():
#     data = {'email': 'francisco.fariasneto14@gmail.com'}
#     response = client.get("/create_token")

#     token = response.json().get("token")
#     return token

def test_get_users():
    # token = get_auth_token()
    headers = {"Authorization": "eyJhbGciOiJIUzI1NiIsInR5cCI6IkpXVCJ9.eyJlbWFpbCI6ImZyYW5jaXNjby5mYXJpYXNuZXRvMTRAZ21haWwuY29tIn0._32Li2OYF1gcIcAu0Ra0KC3tzPJ-JwykhJOw1Mj-fZc"}

    response = client.get("/users", headers=headers)

    assert response.status_code == 200
    assert isinstance(response.json(), list)


# class UserCreate(BaseModel):
#     name: str
#     email: EmailStr
#     token: Optional[str] = None
def test_create_user():
    user_data = {"name": "Francisco", "email": "francisco@fticonsult.com.br"}

    response = client.post("/users", json=user_data, headers=headers)

    assert response.status_code == 200

    data = response.json()

    assert data["message"] == "User created"
    assert data["user"]["name"] == user_data["name"]
    assert data["user"]["email"] == user_data["email"]

def test_get_users():
    response = client.get("/users", headers=headers)
    assert response.status_code == 200
    assert isinstance(response.json(), list)

def test_update_user():
    user_data = {"name": "Francisco", "email": "francisco.fariasneto14@gmail.com"}
    response = client.put("/users/9", json=user_data, headers=headers)
    assert response.status_code == 200
    data = response.json()
    assert data["user"]["email"] == user_data["email"]

def test_delete_user():
    response = client.delete("/users/9", headers=headers)
    assert response.status_code == 200
    data = response.json()
    assert data["message"] == "User deleted"

def test_get_nonexistent_user():
    response = client.get("/Users/9999", headers=headers)
    assert response.status_code == 404

def test_create_user_missing_name():
    ivalid_data = {"email": "teste@gmail.com"}
    response = client.post("/users", json=ivalid_data, headers=headers)
    assert response.status_code == 422
