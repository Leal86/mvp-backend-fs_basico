from pydantic import BaseModel


class ChamadoRequest(BaseModel):
    """
    Schema de entrada para criação de chamado.
    """
    titulo: str
    descricao: str
    id_usuario: int
    prioridade: str | None = "media"


class ChamadoUpdateRequest(BaseModel):
    """
    Schema de entrada para atualização de chamado.
    Todos os campos são opcionais.
    """
    titulo: str | None = None
    descricao: str | None = None
    status: str | None = None
    prioridade: str | None = None