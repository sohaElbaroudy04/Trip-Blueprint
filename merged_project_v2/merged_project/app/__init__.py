from flask import Flask
from flask_sqlalchemy import SQLAlchemy
from flask_login import LoginManager

db = SQLAlchemy()
login_manager = LoginManager()

def create_app():
    app = Flask(__name__, template_folder='templates', static_folder='static')

    app.config['SECRET_KEY'] = 'mysecretkey123'
    app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///app.db'
    app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False

    db.init_app(app)
    login_manager.init_app(app)
    login_manager.login_view = 'auth.login'

    from app.routes.auth_routes import auth_bp
    from app.routes.trip_routes import trip_bp
    from app.routes.community_routes import community_bp
    from app.routes.place_routes import place_bp

    app.register_blueprint(auth_bp)
    app.register_blueprint(trip_bp)
    app.register_blueprint(community_bp)
    app.register_blueprint(place_bp)

    with app.app_context():
        db.create_all()

    return app
