from .base import BaseRepository
from db.schemas.users import UsersTable
from sqlalchemy.orm import Session


class UsersTableRepository(BaseRepository):
    table = UsersTable

    async def get_user_by_id(self, user_id: int, session: Session):
        user = self.get("id", value=user_id, session=session)

        return user