from flask import Flask
from flask_sqlalchemy import SQLAlchemy
from flask_migrate import Migrate

# initilizing sqlalchemy instance
db = SQLAlchemy()


def create_app():
    app = Flask(__name__)
    app.config.from_object('Config')
    db.init_app(app)                # configure sqlalchemy instance to work with Flask app
    migrate = Migrate(app, db)

    # initilizing the security
    from flask_security import Security, SQLAlchemyUserDatastore
    from .auth.models import User, Role

    user_datastore = SQLAlchemyUserDatastore(db, User, Role)
    security = Security(app, user_datastore)

    # define BluePrints
    from .routes.men import men
    from .routes.women import women
    from app.routes.Admin import admin
    from app.routes.front_routes import bp

    app.register_blueprint(bp)
    app.register_blueprint(women)
    app.register_blueprint(men)
    app.register_blueprint(admin)

    return app
