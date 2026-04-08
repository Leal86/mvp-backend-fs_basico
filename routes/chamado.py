from flask import Blueprint, request, jsonify
from models import Chamado, Usuario, db
from schemas import (
    chamado_schema,
    lista_chamados_schema,
    erro_schema,
    mensagem_schema
)
from schemas.request.chamado import ChamadoRequest, ChamadoUpdateRequest
from pydantic import ValidationError
from logger import logger

# Criação do Blueprint para rotas de chamado
chamado_bp = Blueprint("chamado", __name__)


# ================================================== #
#                ROTAS PARA CHAMADOS                 #
# ================================================== #

# Rota para criar um novo chamado.
@chamado_bp.route("/chamados", methods=["POST"])
def criar_chamado():
    """
    Cria um novo chamado.

    O chamado deve estar vinculado a um usuário existente.
    """
    try:
        try:
            data = ChamadoRequest(**request.json)
        except ValidationError as e:
            return jsonify({"error": e.errors()}), 400

        usuario = Usuario.query.get(data.id_usuario)
        if not usuario:
            return jsonify(erro_schema("Usuário informado não existe.")), 404

        chamado = Chamado(
            titulo=data.titulo,
            descricao=data.descricao,
            prioridade=data.prioridade,
            id_usuario=data.id_usuario,
        )

        db.session.add(chamado)
        db.session.commit()

        logger.debug("Chamado criado com sucesso.")
        return jsonify(chamado_schema(chamado)), 201

    except Exception as e:
        logger.error(f"Erro ao criar chamado: {e}")
        return jsonify(erro_schema("Erro ao criar chamado.")), 500


# Rota para listar todos os chamados cadastrados.
@chamado_bp.route("/chamados", methods=["GET"])
def listar_chamados():
    """
    Lista todos os chamados cadastrados.
    """
    try:
        chamados = Chamado.query.all()
        logger.debug("Listagem de chamados realizada com sucesso.")
        return jsonify(lista_chamados_schema(chamados)), 200

    except Exception as e:
        logger.error(f"Erro ao listar chamados: {e}")
        return jsonify(erro_schema("Erro ao listar chamados.")), 500


# Rota para buscar um chamado específico pelo ID.
@chamado_bp.route("/chamados/<int:id>", methods=["GET"])
def buscar_chamado(id):
    """
    Busca um chamado pelo ID.
    """
    try:
        chamado = Chamado.query.get(id)

        if not chamado:
            return jsonify(erro_schema("Chamado não encontrado.")), 404

        logger.debug(f"Chamado {id} encontrado com sucesso.")
        return jsonify(chamado_schema(chamado)), 200

    except Exception as e:
        logger.error(f"Erro ao buscar chamado: {e}")
        return jsonify(erro_schema("Erro ao buscar chamado.")), 500


# Rota para atualizar os dados de um chamado existente.
@chamado_bp.route("/chamados/<int:id>", methods=["PUT"])
def atualizar_chamado(id):
    """
    Atualiza os dados de um chamado.

    Atualmente permite atualizar título, descrição, status e prioridade.
    """
    try:
        chamado = Chamado.query.get(id)

        if not chamado:
            return jsonify(erro_schema("Chamado não encontrado.")), 404

        try:
            data = ChamadoUpdateRequest(**request.json)
        except ValidationError as e:
            return jsonify({"error": e.errors()}), 400

        if data.titulo is not None:
            chamado.titulo = data.titulo
        if data.descricao is not None:
            chamado.descricao = data.descricao
        if data.status is not None:
            chamado.status = data.status
        if data.prioridade is not None:
            chamado.prioridade = data.prioridade

        db.session.commit()

        logger.debug(f"Chamado {id} atualizado com sucesso.")
        return jsonify(chamado_schema(chamado)), 200

    except Exception as e:
        logger.error(f"Erro ao atualizar chamado: {e}")
        return jsonify(erro_schema("Erro ao atualizar chamado.")), 500


# Rota para deletar um chamado pelo ID.
@chamado_bp.route("/chamados/<int:id>", methods=["DELETE"])
def deletar_chamado(id):
    """
    Remove um chamado pelo ID.
    """
    try:
        chamado = Chamado.query.get(id)

        if not chamado:
            return jsonify(erro_schema("Chamado não encontrado.")), 404

        db.session.delete(chamado)
        db.session.commit()

        logger.debug(f"Chamado {id} removido com sucesso.")
        return jsonify(mensagem_schema("Chamado deletado com sucesso.")), 200

    except Exception as e:
        logger.error(f"Erro ao deletar chamado: {e}")
        return jsonify(erro_schema("Erro ao deletar chamado.")), 500