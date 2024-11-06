from .router import router
from API.config import create_session
from fastapi import Depends, Body
from sqlalchemy.orm import Session
from db.schemas.users import UsersTable

from pydantic import BaseModel


class CreateUserSchema(BaseModel):
    first_name: str
    last_name: str
    email: str
    password: str



@router.post("/create/")
async def create_user(data: CreateUserSchema = Body(), session: Session = Depends(create_session)):
    with session:
        user = UsersTable(**data.dict())

        with session:
            session.add(user)
            session.commit()
            session.refresh(user)

        return {"user": user}

