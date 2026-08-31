from sqlalchemy import ForeignKey
from sqlalchemy.orm import Mapped, mapped_column

from repository.database import Base

class FundInvestor(Base):
    __tablename__ = "fund_investors"

    fund_id: Mapped[int] = mapped_column(ForeignKey("funds.id"), primary_key=True)
    investor_id: Mapped[int] = mapped_column(ForeignKey("investors.id"), primary_key=True)
    shares: Mapped[float]