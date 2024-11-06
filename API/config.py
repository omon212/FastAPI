from db.config import SessionLocal


async def create_session():
    with SessionLocal() as session:
        yield session