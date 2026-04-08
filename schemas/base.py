# ================================================== #
#                 MENSAGENS PADRÃO                   #
# ================================================== #

def mensagem_schema(msg):
    """
    Retorna uma mensagem padrão de sucesso.
    """
    return {
        "message": msg
    }


def erro_schema(msg):
    """
    Retorna uma mensagem padrão de erro.
    """
    return {
        "error": msg
    }