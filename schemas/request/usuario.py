from pydantic import BaseModel

class UsuarioRequest(BaseModel):
    """
    Schema de entrada para criação/atualização de usuário.
    """

    nome: str
    id_depto: int
    matricula: str | None = None
    funcao: str | None = None