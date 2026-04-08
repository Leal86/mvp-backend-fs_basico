from pydantic import BaseModel


class DepartamentoRequest(BaseModel):
    """
    Schema de entrada para criação e atualização de departamento.
    """
    nome: str
    sigla: str | None = None
    telefone: str | None = None
    
class DepartamentoUpdateRequest(BaseModel):
    """
    Schema de entrada para atualização de departamento.
    Todos os campos são opcionais.
    """
    nome: str | None = None
    sigla: str | None = None
    telefone: str | None = None