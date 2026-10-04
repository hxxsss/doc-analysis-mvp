import json
import os

from dotenv import load_dotenv
from google.oauth2 import service_account


load_dotenv()

_GCP_SCOPES = ["https://www.googleapis.com/auth/cloud-platform"]

class CredentialProvider:
    @staticmethod
    def _require_env(var_name: str) -> str:
        value = os.getenv(var_name)
        if not value:
            raise ValueError(f"Erro: {var_name} não encontrado no .env!")
        return value

    @staticmethod
    def get_gcp_credentials() -> service_account.Credentials:
        credentials_json = CredentialProvider._require_env("GCP_CREDENTIALS_JSON")
        return service_account.Credentials.from_service_account_info(
            json.loads(credentials_json), scopes=_GCP_SCOPES
        )

    @staticmethod
    def get_database_url() -> str:
        return CredentialProvider._require_env("DATABASE_URL")