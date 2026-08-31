from sqlalchemy import String, ForeignKey
from sqlalchemy.orm import Mapped, mapped_column

from repository.database import Base


class Investor(Base):
    __tablename__ = "investors"

    id: Mapped[int] = mapped_column(primary_key=True)
    name: Mapped[str] = mapped_column(String(255))
    document: Mapped[str] = mapped_column(String(14), unique=True)
    signer_group_id: Mapped[int] = mapped_column(ForeignKey("signer_groups.id"))