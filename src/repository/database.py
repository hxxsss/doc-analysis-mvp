from sqlalchemy import create_engine
from sqlalchemy.orm import DeclarativeBase, sessionmaker

from utils.credentials_provider import CredentialProvider


class Base(DeclarativeBase):
    """Classe base de herança ORM."""

_engine = create_engine(
    CredentialProvider.get_database_url(),
    pool_pre_ping=True,   
    pool_size=5,
    max_overflow=10,
    echo=False,           
)

SessionLocal = sessionmaker(bind=_engine, expire_on_commit=False)