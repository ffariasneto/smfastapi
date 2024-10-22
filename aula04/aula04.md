# Criar pasta venv
python -m venv venv

# Ativar pasta venv
source venv/Scripts/activate

# Instalar FastAPI e Uvicorn
pip install fastapi uvicorn

# Listar todas as bibliotecas instaladas
pip freeze > requirements.txt

# Iniciar Uvicorn
uvicorn main:app --reload

# API Rest com FASTAPI
## Arquitetura REST
REST (Representational State Transfer) é uma forma de estruturar e criar uma API.
Cada Requisição é independente das outras.
### Princípios Fundamentais
- Statelessness (Ausência de estado): Uma API REST deve ser projetada para que cada requisição seja completa por si só.
O cliente envia todas as informações necessárias para que o servidor responda de forma independente.
- Uniform Interface (Interface Uniforme): Todas as interações entre cliente e servidor seguem padrões uniformes. As URLs, o métodos (HTTP(GET, POST, PUT, DELETE)) e o formatos de dados são geralmente JSON.
- Client Server: define uma separação clara entre o cliente e o servidor em uma arquitetura REST. O cliente é responsável por enviar requisoções HTTP para o servidor, que processa essas requisções e retorna respostas.
### Recursos e URLS
Uma das principais características da API REST é a forma que ela trata os recursos, que são os objetos ou coleções de objetos retornados para o cliente quando ele faz a solicitação.
### Verbos HTTP e Status Code
Os verbos HTTP são fundamentais.
- GET
- POST
- PUT
- DELETE
Status Code, indicam o resultado da operação
- 2xx: Sucesso
- 4xx: Erros do cliente,
- 5xx: Erros de servidor.
### Modularização de uma API REST
A modularização das funcionalidades de uma API REST é crucial para a qualidade da comunicação entre sistemas.
### Routes
As rotas (ou endpoints) são os caminhos pelos quais os clientes interagem com a API.
Cada rota é associada a um caminho URL específico e uma função que processa a requisição.
O include_router é uma função do FastAPI que permite incluir um conjunto de rotas.
### Schemas
São utilizados para definir a estrutura e a validação dos dados que uma API recebe e retorna.
Schemas são implementados com Pydantic, que permite criar modelos de dados com validação automática.
### CRUD
CRUD é um acrônimo que representa as quatro operações básicas que é possível realizar em dados em um sistema:
- Create (Criar)
- Read (Ler/Consultar)
- Update (Atualizar)
- Delete (Deletar)