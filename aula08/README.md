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

pip install pytest
```
# Iniciar Uvicorn
```
uvicorn main:app --reload
```
# Testar API
```
http://127.0.0.1:8000/docs
```

# Testes automatizados
São processos sistemáticos de verificação e validação que garantem que um sistema, software ou produto atenda aos requisitos e funcione corretamente.
Em APIs, os testes visam verificar o funcionamento correto de endpoints, garantindo que a aplicação responda conforme esperado.

## Tipos de testes
### Testes de unidade
Verificam o funcionamento de componentes individuais da API
### Testes de integração
Validam a interação entre diferentes componentes
### Testes de Ponta a Ponta

## Testes FASTAPI
### Estrutura dos arquivos de testes
Os arquivos de teste devem seguir o padrão de nome test_*.py (test_main.py) ou *_test.py (user_test.py) para que o Pytest detecte os arquivos automaticamente.
