# app/__init__.py

from flask import Flask
from .routes import routes
from .logging import setup_logging  # Import setup_logging from logging
from .config import Config  # Import Config from config

def create_app():
    app = Flask(__name__)
    app.config.from_object(Config)  # Use Config to load the settings

    # Set up logging
    setup_logging()

    # Register blueprints or routes
    app.register_blueprint(routes)
    
    return app
