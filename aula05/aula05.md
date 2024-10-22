# Criar pasta venv
python -m venv venv

# Ativar pasta venv
source venv/Scripts/activate

# Instalar FastAPI e Uvicorn
pip install fastapi uvicorn sqlmodel pymysql

# Listar todas as bibliotecas instaladas
pip freeze > requirements.txt

# Iniciar Uvicorn
uvicorn main:app --reload