from . import db    
# ================================================== #
#                   DEPARTAMENTO                     #
# ================================================== #
class Departamento(db.Model):
    """
    Representa um departamento da organização.

    Um departamento pode possuir vários usuários.
    """
    __tablename__ = 'departamentos'

    id = db.Column(db.Integer, primary_key=True)
    nome = db.Column(db.String(100), nullable=False)
    sigla = db.Column(db.String(10))
    telefone = db.Column(db.String(20))

    # relacionamento com usuários
    usuarios = db.relationship('Usuario', backref='departamento', lazy=True)

    def __repr__(self):
        return f"<Departamento {self.nome}>"