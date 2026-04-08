from . import db

# ================================================== #
#                       USUARIO                      #
# ================================================== #
class Usuario(db.Model):
    """
    Representa um usuário do sistema.

    Um usuário pertence a um departamento e pode abrir vários chamados.
    """
    __tablename__ = 'usuarios'

    id = db.Column(db.Integer, primary_key=True)
    nome = db.Column(db.String(100), nullable=False)
    matricula = db.Column(db.String(50))
    funcao = db.Column(db.String(50))

    # chave estrangeira para departamento
    id_depto = db.Column(db.Integer, db.ForeignKey('departamentos.id'), nullable=False)

    # relacionamento com chamados
    chamados = db.relationship('Chamado', backref='usuario', lazy=True)

    def __repr__(self):
        return f"<Usuario {self.nome}>"