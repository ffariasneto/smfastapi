from sqlmodel import SQLModel, create_engine, Session

DATABASE_URL = "mysql+pymysql://root:@localhost:3306/bd_teste"

engine = create_engine(DATABASE_URL, echo=True)

def get_session():
    with Session(engine) as session:
        yield session

def create_table():
    SQLModel.metadata.create_all(engine)
