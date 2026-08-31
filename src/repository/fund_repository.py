from sqlalchemy import select
from sqlalchemy.orm import Session

from models.investor import Investor
from models.fund import Fund
from models.fund_investor import FundInvestor



class FundRepository:
    def __init__(self, session: Session):
        self._session = session

    def get_by_id(self, fund_id: int) -> Fund | None:
        return self._session.get(Fund, fund_id)

    def get_by_doc(self, fund_doc: str) -> Fund | None:
        statement = select(Fund).where(Fund.document == fund_doc)
        return self._session.scalars(statement).first()

    def get_investors(self, fund_doc) -> list[Investor]:
        statement = (
            select(Investor)
            .join(FundInvestor, FundInvestor.investor_id == Investor.id)
            .join(Fund, Fund.id == FundInvestor.fund_id)
            .where(Fund.document == fund_doc)
        )
        return list(self._session.scalars(statement).all())