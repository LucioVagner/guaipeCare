from flask import Blueprint

# Blueprint agrupa as rotas públicas (acessíveis sem login).
# O primeiro argumento é o nome interno usado pelo Flask para identificar o blueprint.
public = Blueprint("public", __name__)


@public.route("/a/<tag>")
def pagina_animal(tag):
    """Rota pública acessada pela tag NFC da coleira.

    Por enquanto devolve a tag em texto puro.
    Nos próximos passos buscará o animal no banco e renderizará o template.
    """
    return f"Tag recebida: {tag}"
