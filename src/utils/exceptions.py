class VertexAiConnectorError(Exception):
    """Erro base para falhas de comunicação com o Vertex AI."""


class VertexAiRequestError(VertexAiConnectorError):
    """A chamada à API falhou (rede, autenticação, quota, etc)."""


class VertexAiResponseValidationError(VertexAiConnectorError):
    """A resposta do modelo não pôde ser validada contra o schema esperado."""