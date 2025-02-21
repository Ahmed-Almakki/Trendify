import os
from flask import Flask
from flask_sqlalchemy import SQLAlchemy
from dotenv import load_dotenv  # load the enviromental variable

# initilizing sqlalchemy instance
db = SQLAlchemy()


def create_app():
    load_dotenv()
    app = Flask(__name__)
    app.config['SQLALCHEMY_DATABASE_URI'] = os.getenv('DATABASE_URI')  # configuration loaded from config file
    db.init_app(app)                # configure sqlalchemy instance to work with Flask app

    from .routes.men import men
    from app.routes.Admin import admin
    from app.routes.front_routes import bp

    app.register_blueprint(bp)
    app.register_blueprint(men)
    app.register_blueprint(admin)

    from .models import Clothing, Top, Bottom, Category
    with app.app_context():
        db.create_all()

    return app
