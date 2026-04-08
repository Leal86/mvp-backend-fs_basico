# ================================================== #
#                   DEPARTAMENTO                     #
# ================================================== #

def departamento_schema(departamento):
    """
    Formata um departamento para resposta.
    """
    return {
        "id": departamento.id,
        "nome": departamento.nome,
        "sigla": departamento.sigla,
        "telefone": departamento.telefone
    }


def lista_departamentos_schema(departamentos):
    """
    Retorna lista de departamentos formatados.
    """
    return [departamento_schema(d) for d in departamentos]