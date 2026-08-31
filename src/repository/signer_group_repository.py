from sqlalchemy.orm import Session

from models.signer_group import SignerGroup


class SignerGroupRepository:
    def __init__(self, session: Session):
        self._session = session

    def get_by_id(self, signer_group_id: int) -> SignerGroup | None:
        return self._session.get(SignerGroup, signer_group_id)

    def get_signers(self, signer_group_id: int) -> list[dict]:
        group = self.get_by_id(signer_group_id)
        return group.signers if group else []