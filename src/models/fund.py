from sqlalchemy import String
from sqlalchemy.orm import Mapped, mapped_column

from repository.database import Base


class Fund(Base):
    __tablename__ = "funds"

    id: Mapped[int] = mapped_column(primary_key=True)
    name: Mapped[str] = mapped_column(String(255))
    document: Mapped[str] = mapped_column(String(14), unique=True)