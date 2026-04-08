from flask import Blueprint, request, jsonify
from models import Usuario, Departamento, db
from schemas import (
    usuario_schema,
    lista_usuarios_schema,
    erro_schema,
    mensagem_schema
)
from schemas.request.usuario import UsuarioRequest
from pydantic import ValidationError
from logger import logger

# Criação do Blueprint para rotas de usuário
usuario_bp = Blueprint("usuario", __name__)

# ================================================== #
#                ROTAS PARA USUÁRIOS                 #
# ================================================== #

# Rota para criar um novo usuário.
@usuario_bp.route("/usuarios", methods=["POST"])
def criar_usuario():
    """
    Cria um novo usuário.

    O usuário deve estar vinculado a um departamento existente.
    """
    try:
        try:
            data = UsuarioRequest(**request.json)
        except ValidationError as e:
            return jsonify({"error": e.errors()}), 400

        departamento = Departamento.query.get(data.id_depto)
        if not departamento:
            return jsonify(erro_schema("Departamento informado não existe.")), 404

        usuario = Usuario(
            nome=data.nome,
            matricula=data.matricula,
            funcao=data.funcao,
            id_depto=data.id_depto,
        )

        db.session.add(usuario)
        db.session.commit()

        logger.debug("Usuário criado com sucesso.")
        return jsonify(usuario_schema(usuario)), 201

    except Exception as e:
        logger.error(f"Erro ao criar usuário: {e}")
        return jsonify(erro_schema("Erro ao criar usuário.")), 500
    
# Rota para listar todos os usuários cadastrados.
@usuario_bp.route("/usuarios", methods=["GET"])
def listar_usuarios():
    """
    Lista todos os usuários cadastrados.
    """
    try:
        usuarios = Usuario.query.all()
        logger.debug("Listagem de usuários realizada com sucesso.")
        return jsonify(lista_usuarios_schema(usuarios)), 200

    except Exception as e:
        logger.error(f"Erro ao listar usuários: {e}")
        return jsonify(erro_schema("Erro ao listar usuários.")), 500


# Rota para buscar um usuário específico pelo ID.
@usuario_bp.route("/usuarios/<int:id>", methods=["GET"])
def buscar_usuario(id):
    """
    Busca um usuário pelo ID.
    """
    try:
        usuario = Usuario.query.get(id)

        if not usuario:
            return jsonify(erro_schema("Usuário não encontrado.")), 404

        logger.debug(f"Usuário {id} encontrado com sucesso.")
        return jsonify(usuario_schema(usuario)), 200

    except Exception as e:
        logger.error(f"Erro ao buscar usuário: {e}")
        return jsonify(erro_schema("Erro ao buscar usuário.")), 500


# Rota para atualizar os dados de um usuário existente.
@usuario_bp.route("/usuarios/<int:id>", methods=["PUT"])
def atualizar_usuario(id):
    """
    Atualiza os dados de um usuário.
    """
    try:
        usuario = Usuario.query.get(id)

        if not usuario:
            return jsonify(erro_schema("Usuário não encontrado.")), 404

        data = request.json

        if "id_depto" in data:
            departamento = Departamento.query.get(data["id_depto"])
            if not departamento:
                return jsonify(erro_schema("Departamento informado não existe.")), 404
            usuario.id_depto = data["id_depto"]

        usuario.nome = data.get("nome", usuario.nome)
        usuario.matricula = data.get("matricula", usuario.matricula)
        usuario.funcao = data.get("funcao", usuario.funcao)

        db.session.commit()

        logger.debug(f"Usuário {id} atualizado com sucesso.")
        return jsonify(usuario_schema(usuario)), 200

    except Exception as e:
        logger.error(f"Erro ao atualizar usuário: {e}")
        return jsonify(erro_schema("Erro ao atualizar usuário.")), 500


# Rota para deletar um usuário pelo ID.
@usuario_bp.route("/usuarios/<int:id>", methods=["DELETE"])
def deletar_usuario(id):
    """
    Remove um usuário pelo ID.
    """
    try:
        usuario = Usuario.query.get(id)

        if not usuario:
            return jsonify(erro_schema("Usuário não encontrado.")), 404

        db.session.delete(usuario)
        db.session.commit()

        logger.debug(f"Usuário {id} removido com sucesso.")
        return jsonify(mensagem_schema("Usuário deletado com sucesso.")), 200

    except Exception as e:
        logger.error(f"Erro ao deletar usuário: {e}")
        return jsonify(erro_schema("Erro ao deletar usuário.")), 500