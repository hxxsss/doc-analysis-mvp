from sqlalchemy.dialects.postgresql import JSONB
from sqlalchemy.orm import Mapped, mapped_column

from repository.database import Base


class SignerGroup(Base):
    __tablename__ = "signer_groups"

    id: Mapped[int] = mapped_column(primary_key=True)
    signers: Mapped[list[dict]] = mapped_column(JSONB)
    