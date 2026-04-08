from flask_sqlalchemy import SQLAlchemy

# Instância única do banco
db = SQLAlchemy()

# Importação dos models
from .departamento import Departamento
from .usuario import Usuario
from .chamado import Chamado