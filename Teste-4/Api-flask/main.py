from flask import Flask
from flask_cors import CORS  # Importa o CORS
from app import create_app  # Supondo que você tenha uma função create_app

app = create_app()

# Habilita CORS para todas as rotas
CORS(app)

if __name__ == '__main__':
    app.run(debug=True)