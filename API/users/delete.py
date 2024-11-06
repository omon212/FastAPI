from .router import router
from fastapi import Depends
from sqlalchemy.orm import Session
from sqlalchemy import delete, select
from db.schemas.users import UsersTable
from API.config import create_session


@router.delete("/delete/{user_id}")
async def delete_user(user_id: int, session: Session = Depends(create_session)):
    with session:
        query_get_user = select(UsersTable).where(UsersTable.id == user_id)
        user = (session.execute(query_get_user)).scalar_one_or_none()

        if user:
            query_delete_user = delete(UsersTable).where(UsersTable.id == user_id)
            user = session.execute(query_delete_user)
            session.commit()

            return {"message": "Deleted successfully!"}
        else:
            return {"message": "User not found"}