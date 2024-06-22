from flask import Flask
import os

from config import config

def create_app(config_class=config):
    app = Flask(__name__)
    app.config.from_object(config_class[os.getenv('FLASK_ENV', 'dev')])

    # Initialize Flask extensions here

    # Register blueprints
    from app.main import bp as main_bp
    app.register_blueprint(main_bp)

    return app