# app/__init__.py

from flask import Flask
from .routes import routes
import .config from Config # Import Config from config

def create_app():
    app = Flask(__name__)
    app.config.from_object(Config) # Use Config to load the settings
    app.register_blueprint(routes)
    return app
