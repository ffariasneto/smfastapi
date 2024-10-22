## Tipos de API
- APIs RESTful (Representational State Transfer)
- APIs GraphQL
- APIs SOAP (Simple Object Access Protocol)
## O que é HTTP
É o protocolo de comunicação que permite a trica de informações entre navegadores web e servidores web.
### Métodos HTTP
- GET
- POST
- PUT
- DELETE
## REQUEST
### REQUEST - Componentes
- Método HTTP
- URL
- Headers
- Body
## RESPONSE
É a resposta do servidor à request.
### RESPONSE - Componentes
- Status Code
- Headers
- Body
## JSON
Javascript Object Notation - é um formato leve de troca de dados e usado para comunicação entre sistemas, especialmente em aplicações web.
A estrutura do JSON é similar a pares chave-valor, mas ele é sempre uma string formatada, podendo ser convertida para tipos nativos, como dicionários, em várias linguagens de programação.
OBS: No JSON só é possível usar aspas duplas.
### DummyJSON
https://dummyjson.com/
# FASTAPI
É um framework Python moderno e de alto desempenho, ideal para construir APIs web.
Ele oferece recursos como tipagem estática, validação de dados, documentação automática e integração com banco de dados.
Projetado para ser rápido, fácil de usar e eficiente.
# Criando ambiente virtual
## No Git Bash
Comando python -m venv venv
## Ativar ambiente virtual
source venv/Scripts/activate
## Instalar FASTAPI e UVICORN
pip install fastapi uvicorn