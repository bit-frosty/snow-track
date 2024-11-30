import os
from flask import Flask
from .database import init_db
from .tracker import init_tracking_system

def create_app():
    """Initialize the Flask app."""
    app = Flask(__name__)
    app.config['SECRET_KEY'] = os.getenv('SECRET_KEY')
    app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///frostbytectf.db'
    app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False

    # Initialize database
    init_db()

    # Initialize tracking system
    init_tracking_system()

    with app.app_context():
        from .routes import bp as main_blueprint
        app.register_blueprint(main_blueprint)

    return app
