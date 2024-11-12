import jwt
from fastapi import Request, HTTPException

SECRET_KEY = "teste_de_senha"
ALGORITHM = "HS256"

def create_token(dados: dict):
    token = jwt.encode(dados, SECRET_KEY, ALGORITHM)
    return token

def auth(request: Request, call_next):

    if request.url == "http://127.0.0.1:8000/":
        return call_next(request)
    
    token = request.headers.get("Authorization")

    if not token:
        raise HTTPException(status_code=401, detail="Token not found")
    
    payload = jwt.decode(token, SECRET_KEY, algorithms=[ALGORITHM])

    if payload:
        return call_next(request)
    else:
        raise HTTPException(status_code=401, detail="Invalid Token")

# def auth(request: Request, call_next):
#     # Obter o token do cabeçalho de autorização
#     token = request.headers.get("Authorization")

#     if not token:
#         raise HTTPException(status_code=401, detail="Token not found")
    
#     # Verificar se o token começa com "Bearer"
#     if not token.startswith("Bearer "):
#         raise HTTPException(status_code=401, detail="Invalid token format")
    
#     # Extrair apenas o token (remover "Bearer " do começo)
#     token = token[len("Bearer "):]

#     try:
#         # Tentar decodificar o JWT com a chave secreta e o algoritmo
#         payload = jwt.decode(token, SECRET_KEY, algorithms=[ALGORITHM])
#     except jwt.ExpiredSignatureError:
#         raise HTTPException(status_code=401, detail="Token has expired")
#     except jwt.JWTClaimsError:
#         raise HTTPException(status_code=401, detail="Invalid claims, please check the token")
#     except jwt.PyJWTError:
#         raise HTTPException(status_code=401, detail="Invalid token")

#     # Se o token for válido, permitir que a requisição continue
#     return call_next(request)