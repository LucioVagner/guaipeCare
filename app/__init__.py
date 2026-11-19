from flask import Flask
from config import Config


def create_app():
    """Application Factory: cria e configura o app Flask.

    Usar uma função (em vez de criar o app no nível do módulo) evita
    importações circulares e facilita testes no futuro.
    """
    app = Flask(__name__)

    # Carrega as configurações definidas em config.py
    app.config.from_object(Config)

    # Importa e registra o blueprint das rotas públicas.
    # A importação é feita aqui dentro para evitar import circular
    # (os blueprints importam 'app', que importaria 'blueprints' no topo).
    from app.routes_public import public
    app.register_blueprint(public)

    return app
