from google import genai
from typing import TypeVar
from google.genai import types
from pydantic import BaseModel
from google.genai import errors as genai_errors

from utils.credentials_provider import CredentialProvider
from utils.exceptions import (
    VertexAiRequestError,
    VertexAiResponseValidationError,
)


_DEFAULT_MODEL = "gemini-3-flash"

T = TypeVar("T", bound=BaseModel)

class VertexAiConnector:
    def __init__(self, model: str = _DEFAULT_MODEL):
        self._model = model
        self._gcp_credentials = CredentialProvider.get_gcp_credentials()
        self._client = genai.Client(
            vertexai=True,
            project=self._gcp_credentials.project_id,
            location="global",
            credentials=self._gcp_credentials,
        )

    def analyze_pdf(self, pdf_bytes: bytes, prompt: str, response_model: type[T]) -> T:
        pdf_part = types.Part.from_bytes(data=pdf_bytes, mime_type="application/pdf")
        response = self._generate_content(pdf_part, prompt, response_model)
        return self._parse_response(response, response_model)

    def _generate_content(self, pdf_part: types.Part, prompt: str, response_model: type[T]) -> types.GenerateContentResponse:
        try:
            return self._client.models.generate_content(
                model=self._model,
                contents=[pdf_part, prompt],
                config=types.GenerateContentConfig(
                    response_mime_type="application/json",
                    response_schema=response_model,
                ),
            )
        except genai_errors.APIError as error:
            raise VertexAiRequestError(
                f"Falha na chamada ao Vertex AI: {error}"
            ) from error

    @staticmethod
    def _parse_response(response: types.GenerateContentResponse, response_model: type[T]) -> T:
        if response.parsed is None:
            raise VertexAiResponseValidationError(
                f"A resposta não pôde ser validada contra {response_model.__name__}."
            )
        return response.parsed