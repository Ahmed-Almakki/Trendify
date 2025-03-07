from flask_session import Session
from flask import Flask
from flask_sqlalchemy import SQLAlchemy
from flask_migrate import Migrate
from flask_security import Security, SQLAlchemyUserDatastore
import stripe

# initilizing sqlalchemy instance
db = SQLAlchemy()

# initialize it outside the function, so it can be imported by other modules
user_datastore = None

# initialize Session from flask_session so the session be on server side "redis"
sess = Session()


def create_app():

    global user_datastore

    app = Flask(__name__)
    app.config.from_object('Config')
    db.init_app(app)                # configure sqlalchemy instance to work with Flask app
    migrate = Migrate(app, db)
    sess.init_app(app)

    stripe.api_key = app.config.get('STRIPE_SECRET_KEY')

    # initilizing the security
    from .auth.models import User, Role

    user_datastore = SQLAlchemyUserDatastore(db, User, Role)
    security = Security(app, user_datastore, register_blueprint=False)

    # define BluePrints
    from .routes.men import men
    from .routes.women import women
    from app.routes.Admin import admin
    from app.auth.auth_routes import auth
    from app.routes.cart import cart
    from app.routes.front_routes import bp

    app.register_blueprint(bp)
    app.register_blueprint(women)
    app.register_blueprint(men)
    app.register_blueprint(admin)
    app.register_blueprint(cart)
    app.register_blueprint(auth)

    with app.app_context():
        db.create_all()

    return app
