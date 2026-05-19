
from flask import Flask
from app.database import init_db
from app.routes import register_routes


def create_app():
    app = Flask(__name__)

    app.config["SECRET_KEY"] = "dev-secret-key"

    init_db()
    register_routes(app)

    return app
