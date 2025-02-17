from flask import Flask
from .front_routes import bp


def create_app():
    app = Flask(__name__)
    app.register_blueprint(bp)
    return app
