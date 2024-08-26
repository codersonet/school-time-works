# app/__init__.py

from flask import Flask
from .routes import routes
import config 

def create_app():
    app = Flask(__name__)
    app.config.from_object(config.Config)
    app.register_blueprint(routes)
    return app
