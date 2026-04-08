from flask import Blueprint, request, jsonify
from models import Departamento, db
from schemas import (
    departamento_schema,
    lista_departamentos_schema,
    erro_schema,
    mensagem_schema
)
from schemas.request.departamento import (
    DepartamentoRequest,
    DepartamentoUpdateRequest
)
from pydantic import ValidationError
from logger import logger

# Criação do Blueprint para rotas de departamento
departamento_bp = Blueprint("departamento", __name__)


# ================================================== #
#             ROTAS PARA DEPARTAMENTOS               #
# ================================================== #

# Rota que permite criar departamentos.
@departamento_bp.route("/departamentos", methods=["POST"])
def criar_departamento():
    """
    Cria um novo departamento.

    Recebe os dados em JSON e salva no banco de dados.
    """
    try:
        try:
            data = DepartamentoRequest(**request.json)
        except ValidationError as e:
            return jsonify({"error": e.errors()}), 400

        departamento = Departamento(
            nome=data.nome,
            sigla=data.sigla,
            telefone=data.telefone
        )

        db.session.add(departamento)
        db.session.commit()

        logger.debug("Departamento criado com sucesso.")
        return jsonify(departamento_schema(departamento)), 201

    except Exception as e:
        logger.error(f"Erro ao criar departamento: {e}")
        return jsonify(erro_schema("Erro ao criar departamento.")), 500

# Rota para listar todos os departamentos cadastrados.
@departamento_bp.route("/departamentos", methods=["GET"])
def listar_departamentos():
    """
    Lista todos os departamentos cadastrados.
    """
    try:
        departamentos = Departamento.query.all()
        logger.debug("Listagem de departamentos realizada com sucesso.")
        return jsonify(lista_departamentos_schema(departamentos)), 200

    except Exception as e:
        logger.error(f"Erro ao listar departamentos: {e}")
        return jsonify(erro_schema("Erro ao listar departamentos.")), 500


# Rota para buscar um departamento específico pelo ID.
@departamento_bp.route("/departamentos/<int:id>", methods=["GET"])
def buscar_departamento(id):
    """
    Busca um departamento pelo ID.
    """
    try:
        departamento = Departamento.query.get(id)

        if not departamento:
            return jsonify(erro_schema("Departamento não encontrado.")), 404

        logger.debug(f"Departamento {id} encontrado com sucesso.")
        return jsonify(departamento_schema(departamento)), 200

    except Exception as e:
        logger.error(f"Erro ao buscar departamento: {e}")
        return jsonify(erro_schema("Erro ao buscar departamento.")), 500


# Rota para atualizar os dados de um departamento existente.
@departamento_bp.route("/departamentos/<int:id>", methods=["PUT"])
def atualizar_departamento(id):
    """
    Atualiza os dados de um departamento.
    """
    try:
        departamento = Departamento.query.get(id)

        if not departamento:
            return jsonify(erro_schema("Departamento não encontrado.")), 404

        try:
            data = DepartamentoUpdateRequest(**request.json)
        except ValidationError as e:
            return jsonify({"error": e.errors()}), 400

        if data.nome is not None:
            departamento.nome = data.nome
        if data.sigla is not None:
            departamento.sigla = data.sigla
        if data.telefone is not None:
            departamento.telefone = data.telefone

        db.session.commit()

        logger.debug(f"Departamento {id} atualizado com sucesso.")
        return jsonify(departamento_schema(departamento)), 200

    except Exception as e:
        logger.error(f"Erro ao atualizar departamento: {e}")
        return jsonify(erro_schema("Erro ao atualizar departamento.")), 500


# Rota para deletar um departamento pelo ID.
@departamento_bp.route("/departamentos/<int:id>", methods=["DELETE"])
def deletar_departamento(id):
    """
    Remove um departamento pelo ID.
    """
    try:
        departamento = Departamento.query.get(id)

        if not departamento:
            return jsonify(erro_schema("Departamento não encontrado.")), 404

        db.session.delete(departamento)
        db.session.commit()

        logger.debug(f"Departamento {id} removido com sucesso.")
        return jsonify(mensagem_schema("Departamento deletado com sucesso.")), 200

    except Exception as e:
        logger.error(f"Erro ao deletar departamento: {e}")
        return jsonify(erro_schema("Erro ao deletar departamento.")), 500