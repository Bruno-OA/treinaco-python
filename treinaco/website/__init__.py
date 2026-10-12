"""Criação da aplicação Flask e suas rotas."""
from pathlib import Path

from flask import Flask, abort, render_template, send_from_directory

from data import buscar_treino, listar_treinos

PUBLIC_DIR = Path(__file__).resolve().parent.parent / "public" / "assets"


def create_app():
    app = Flask(__name__, template_folder="../templates", static_folder=None)

    @app.get("/")
    def inicio():
        return render_template("index.html", treinos=listar_treinos())

    @app.get("/treino/<treino_id>")
    def pagina_treino(treino_id):
        treino = buscar_treino(treino_id)
        if treino is None:
            abort(404)
        return render_template("workout.html", treino=treino, treinos=listar_treinos())

    @app.get("/assets/<path:filename>")
    def arquivos_publicos(filename):
        # Na Vercel, /public/assets é distribuído diretamente pela CDN.
        # Esta rota permite usar exatamente os mesmos links localmente.
        return send_from_directory(PUBLIC_DIR, filename)

    @app.errorhandler(404)
    def nao_encontrado(error):
        return render_template("404.html"), 404

    return app
