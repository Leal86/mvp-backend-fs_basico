# ================================================== #
#                      USUÁRIO                       #
# ================================================== #

def usuario_schema(usuario):
    """
    Formata um usuário para resposta.
    """
    return {
        "id": usuario.id,
        "nome": usuario.nome,
        "matricula": usuario.matricula,
        "funcao": usuario.funcao,
        "departamento": usuario.departamento.nome if usuario.departamento else None
    }


def lista_usuarios_schema(usuarios):
    """
    Retorna lista de usuários formatados.
    """
    return [usuario_schema(u) for u in usuarios]