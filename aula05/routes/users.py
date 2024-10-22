# Importa módulos e funções necessárias do FastAPI e SQLModel
from fastapi import APIRouter, Depends, HTTPException
from sqlmodel import Session, select
from database import get_session  # Função para obter uma sessão de banco de dados
from models.user import User  # Modelo User, representando a tabela de usuários no banco
from schemas.user import UserCreate  # Schema para validação dos dados de criação de usuário

# Cria um roteador para definir rotas de API relacionadas aos usuários
router = APIRouter()

# Define uma rota GET para obter todos os usuários
@router.get("/users")
def get_users(session: Session = Depends(get_session)):
    # Executa uma consulta SELECT para obter todos os usuários do banco de dados
    users = session.exec(select(User)).all()
    # Retorna a lista de usuários
    return users

# Define uma rota GET para obter um usuário específico pelo ID
@router.get("/users/{user_id}")
def get_user(user_id: int, session: Session = Depends(get_session)):
    # Usa o método "get" para obter um usuário pelo seu ID
    user = session.get(User, user_id)
    # Se o usuário não for encontrado, lança uma exceção HTTP 404 (Não encontrado)
    if not user:
        raise HTTPException(status_code=404, detail="User not found")
    # Retorna o usuário encontrado
    return user

# Define uma rota POST para criar um novo usuário
@router.post("/users")
def post_users(user: UserCreate, session: Session = Depends(get_session)):
    # Converte os dados do schema UserCreate para o modelo User, necessário para salvar no banco
    user_db = User(**user.model_dump())

    # Adiciona o novo usuário na sessão (prepara para inserção no banco)
    session.add(user_db)
    # Faz o commit para salvar as mudanças no banco de dados
    session.commit()
    # Atualiza o objeto user_db com quaisquer mudanças automáticas feitas pelo banco (por exemplo, ID gerado automaticamente)
    session.refresh(user_db)

    # Retorna uma mensagem de sucesso e os dados do usuário criado
    return {
        "message": "User created",
        "user": user_db
    }

# Define uma rota PUT para atualizar os dados de um usuário específico pelo ID
@router.put("/users/{user_id}")
def post_user(user: UserCreate, user_id: int, session: Session = Depends(get_session)):
    # Busca o usuário no banco de dados pelo ID
    user_db = session.get(User, user_id)

    # Se o usuário não for encontrado, lança uma exceção HTTP 404 (Não encontrado)
    if not user_db:
        raise HTTPException(status_code=404, detail="User not found")

    # Atualiza os atributos do usuário com os novos valores do schema UserCreate
    user_db.name = user.name
    user_db.email = user.email
    user_db.token = user.token

    # Faz o commit para salvar as mudanças no banco de dados
    session.commit()
    # Atualiza o objeto user_db com quaisquer mudanças feitas pelo banco
    session.refresh(user_db)

    # Retorna o usuário atualizado
    return user_db

# Define uma rota DELETE para excluir um usuário específico pelo ID
@router.delete("/users/{user_id}")
def delete_user(user_id: int, session: Session = Depends(get_session)):
    # Busca o usuário no banco de dados pelo ID
    user_db = session.get(User, user_id)

    # Se o usuário não for encontrado, lança uma exceção HTTP 404 (Não encontrado)
    if not user_db:
        raise HTTPException(status_code=404, detail="User not found")

    # Remove o usuário do banco de dados
    session.delete(user_db)
    # Faz o commit para confirmar a exclusão no banco de dados
    session.commit()

    # Retorna uma mensagem de sucesso confirmando a exclusão
    return {"message": "User deleted"}
