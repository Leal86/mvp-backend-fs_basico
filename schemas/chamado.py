# ================================================== #
#                      CHAMADO                       #
# ================================================== #

def chamado_schema(chamado):
    """
    Formata um chamado para resposta.
    """
    return {
        "id": chamado.id,
        "titulo": chamado.titulo,
        "descricao": chamado.descricao,
        "status": chamado.status,
        "prioridade": chamado.prioridade,
        "usuario": chamado.usuario.nome if chamado.usuario else None,
        "departamento": chamado.usuario.departamento.nome if chamado.usuario and chamado.usuario.departamento else None
    }


def lista_chamados_schema(chamados):
    """
    Retorna lista de chamados formatados.
    """
    return [chamado_schema(c) for c in chamados]