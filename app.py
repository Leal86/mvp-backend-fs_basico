from flask import Flask, redirect, send_from_directory
from flask_swagger_ui import get_swaggerui_blueprint
from flask_cors import CORS
from routes.usuario import usuario_bp
from routes.departamento import departamento_bp
from routes.chamado import chamado_bp
from models import db


# Cria a aplicação Flask
app = Flask(__name__)
CORS(app)
# ================================================== #
#             CONFIGURAÇÃO DO BANCO                  #
# ================================================== #

# Configura o banco de dados SQLite
app.config["SQLALCHEMY_DATABASE_URI"] = "sqlite:///database.db"
app.config["SQLALCHEMY_TRACK_MODIFICATIONS"] = False

# Inicializa o SQLAlchemy com a aplicação Flask
db.init_app(app) 

# Cria as tabelas no banco de dados se elas não existirem
# OBS.: Sem isso, o banco de dados não é criado automaticamente e as tabelas não são geradas.
with app.app_context():
    db.create_all()

# ================================================== #
#              CONFIGURAÇÃO DO SWAGGER               #
# ================================================== #

SWAGGER_URL = "/docs" # URL para acessar a documentação no navegador
API_URL = "/swagger.json" # URL do arquivo de documentação Swagger

swagger_ui = get_swaggerui_blueprint(
    SWAGGER_URL, API_URL, config={"app_name": "API de Chamados"}
)

app.register_blueprint(swagger_ui, url_prefix=SWAGGER_URL)

# ================================================== #
#              REGISTRO DOS BLUEPRINTS               #
# ================================================== #

# Registro do Blueprint para rotas de usuário
app.register_blueprint(usuario_bp)

# Registro do Blueprint para rotas de departamento
app.register_blueprint(departamento_bp)

# Registro do Blueprint para rotas de chamado
app.register_blueprint(chamado_bp)

# ================================================== #
#               ROTAS DE DOCUMENTAÇÃO                #
# ================================================== #

# Rota de configuração inicial para redirecionar para a documentação
@app.route("/")
def home():
    """
    Redireciona para a documentação da API.
    """
    return redirect("/docs")

# Rota para servir o arquivo de documentação Swagger
@app.route("/swagger.json")
def swagger():
    """
    Retorna o arquivo de documentação Swagger.
    """
    return send_from_directory(".", "swagger.json")

# Roda a aplicação Flask
if __name__ == "__main__":
    app.run(debug=True)
