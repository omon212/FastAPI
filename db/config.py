from sqlalchemy import create_engine, Engine
from sqlalchemy.orm import (declarative_base, DeclarativeBase,
                            Session, sessionmaker)


engine: Engine = create_engine("sqlite:///db.sqlite3")

SessionLocal: Session = sessionmaker(autocommit=False, autoflush=False, bind=engine)
Base: DeclarativeBase = declarative_base()


# Base.metadata.create_all(bind=engine) -> migration qilish