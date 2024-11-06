from db.config import Base
from sqlalchemy.orm import Mapped, mapped_column


class UsersTable(Base):
    __tablename__ = 'users_user'

    id: Mapped[int] = mapped_column(index=True, primary_key=True)
    first_name: Mapped[str] = mapped_column()
    last_name: Mapped[str] = mapped_column()
    email: Mapped[str] = mapped_column(unique=True)
    password: Mapped[str] = mapped_column()
