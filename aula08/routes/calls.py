from fastapi import APIRouter, Depends, HTTPException
from sqlmodel import Session, select
from database import get_session
from models.call import Call
from schemas.call import CallCreate
from middlewares import create_token

router = APIRouter()

@router.get("/calls")
def get_calls(session: Session = Depends(get_session)):
    calls = session.exec(select(Call)).all()
    return calls

@router.get("/calls/{call_id}")
def get_call(call_id: int, session: Session = Depends(get_session)):
    call = session.get(Call, call_id)
    if not call:
        raise HTTPException(status_code=404, detail="Call not found")
    return call

@router.post("/calls")
def post_calls(call: CallCreate, session: Session = Depends(get_session)):    
    call_db = Call(**call.model_dump())

    
    session.add(call_db)    
    session.commit()    
    session.refresh(call_db)

    return {
        "message": "Call created",
        "call": call_db
    }

@router.post("/email")
def create_email(email: dict):
    email = {
         "email": "francisco.fariasneto14@gmail.com"
         }
    token = create_token(email)
    return token


@router.put("/calls/{call_id}")
def post_call(call: CallCreate, call_id: int, session: Session = Depends(get_session)):    
    call_db = session.get(Call, call_id)
    
    if not call_db:
        raise HTTPException(status_code=404, detail="Call not found")
    
    call_db.name = call.name
    call_db.email = call.email
    call_db.token = call.token
    
    session.commit()    
    session.refresh(call_db)
    
    return call_db

@router.delete("/calls/{call_id}")
def delete_call(call_id: int, session: Session = Depends(get_session)):    
    call_db = session.get(Call, call_id)
    
    if not call_db:
        raise HTTPException(status_code=404, detail="Call not found")
   
    session.delete(call_db)    
    session.commit()
   
    return {"message": "Call deleted"}