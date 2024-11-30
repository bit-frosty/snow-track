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

    db.init_app(app)
    migrate.init_app(app, db)

    # Setup basic logging
    if not app.debug:
        logging.basicConfig(level=logging.INFO)
        app.logger.addHandler(logging.StreamHandler())

    try:
        # Initialize database (e.g., creating tables if needed)
        init_db()

        # Initialize the asset tracking system
        init_tracking_system()

    except Exception as e:
        app.logger.error(f"Error during app initialization: {e}")
        raise
