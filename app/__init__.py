from flask import Flask
from app.routes.front_routes import bp
from flask_sqlalchemy import SQLAlchemy
from .Config import Config   # load the configuration you need
from dotenv import load_dotenv  # load the enviromental variable

# initilizing sqlalchemy instance
db = SQLAlchemy()


def create_app():
    load_dotenv()
    app = Flask(__name__)
    app.config.from_object(Config)  # configuration loaded from config file
    db.init_app(app)                # configure sqlalchemy instance to work with Flask app

    from .routes.men import men

    app.register_blueprint(bp)
    app.register_blueprint(men)

    with app.app_context():
        db.create_all()

    return app
