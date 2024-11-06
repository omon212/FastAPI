from .router import router
from fastapi import Depends
from sqlalchemy.orm import Session
from API.config import create_session
from sqlalchemy import select, delete
from db.schemas.users import UsersTable


@router.get("/")
async def users_list(session: Session = Depends(create_session)):
    with session:
        query = select(UsersTable)

        users = (session.execute(query)).scalars().all()

    return {"users": users}


@router.get("/{user_id}")
async def user_detail(user_id: int, session: Session = Depends(create_session)):
    with session:
        query = select(UsersTable).where(UsersTable.id == user_id)
        
        user = (session.execute(query)).scalar_one_or_none()
    
    return {"user": user}