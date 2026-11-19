from app import create_app

# Cria a instância do app Flask.
# A variável precisa se chamar "app" para o comando
# "flask --app run run --debug" encontrá-la automaticamente.
app = create_app()
