from flask import Flask
from flask_sqlalchemy import SQLAlchemy
from config import config

db = SQLAlchemy()

def create_app(config_name='default'):
    app = Flask(__name__)
    app.config.from_object(config[config_name])

    db.init_app(app)

    # Importar modelos
    from .models import Conversation

    # Registro de rutas
    from . import routes
    app.register_blueprint(routes.bp)

    return app