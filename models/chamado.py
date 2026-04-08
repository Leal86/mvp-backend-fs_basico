from . import db

# ================================================== #
#                       CHAMADO                      #
# ================================================== #
class Chamado(db.Model):
    """
    Representa um chamado técnico aberto por um usuário.

    Cada chamado pertence a um usuário.
    """
    __tablename__ = 'chamados'

    id = db.Column(db.Integer, primary_key=True)
    titulo = db.Column(db.String(100), nullable=False)
    descricao = db.Column(db.String(200), nullable=False)
    status = db.Column(db.String(50), default='aberto')
    prioridade = db.Column(db.String(50), default='media')

    # chave estrangeira para usuário
    id_usuario = db.Column(db.Integer, db.ForeignKey('usuarios.id'), nullable=False)

    def __repr__(self):
        return f"<Chamado {self.titulo}>"