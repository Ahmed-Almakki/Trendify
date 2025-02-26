from flask import Flask
from flask_sqlalchemy import SQLAlchemy
from flask_migrate import Migrate

# initilizing sqlalchemy instance
db = SQLAlchemy()

# initialize it outside the function, so it can be imported by other modules
user_datastore = None


def create_app():

    global user_datastore

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
    from app.auth.auth_routes import auth
    from app.routes.front_routes import bp

    app.register_blueprint(bp)
    app.register_blueprint(women)
    app.register_blueprint(men)
    app.register_blueprint(admin)
    app.register_blueprint(auth)

    return app
