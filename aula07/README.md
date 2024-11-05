# Instalar a Venv
```
python -m venv venv
```
# Iniciar a Venv
```
source venv/Scripts/activate
```
# Instalar recursos
```
pip install fastapi uvicorn sqlmodel pymysql email-validator pyjwt
```
# Iniciar Uvicorn
```
uvicorn main:app --reload
```
# Testar API
```
http://127.0.0.1:8000/docs
```


