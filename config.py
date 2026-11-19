import os

# Diretório raiz do projeto (onde este arquivo está)
BASE_DIR = os.path.abspath(os.path.dirname(__file__))


class Config:
    # Chave secreta usada pelo Flask para assinar sessões e cookies.
    # Em produção, defina a variável de ambiente SECRET_KEY com um valor forte.
    SECRET_KEY = os.environ.get("SECRET_KEY", "dev-secret-inseguro")

    # Caminho absoluto para o banco de dados SQLite dentro da raiz do projeto.
    SQLALCHEMY_DATABASE_URI = "sqlite:///" + os.path.join(BASE_DIR, "guaipecare.db")

    # Desativa o rastreamento de modificações do SQLAlchemy (economiza memória).
    SQLALCHEMY_TRACK_MODIFICATIONS = False
