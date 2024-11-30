import os
from flask import Flask
from .database import init_db
from .tracker import Tracker
from .utils import validate_input


# Initialize extensions
db = SQLAlchemy()
migrate = Migrate()

def create_app(config_filename=None):
    """Initialize the Flask app with better configuration and logging."""
    app = Flask(__name__)

    # Default Configuration
    app.config['SECRET_KEY'] = os.getenv('SECRET_KEY', 'your-default-secret-key')
    app.config['SQLALCHEMY_DATABASE_URI'] = os.getenv(
        'DATABASE_URL', 'sqlite:///frostbytectf.db')  # Allow DATABASE_URL for prod
    app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False
    # Initialize the database and migration
    db.init_app(app)
    migrate.init_app(app, db)

    # Setup basic logging
    if not app.debug:
        logging.basicConfig(level=logging.INFO)
        app.logger.addHandler(logging.StreamHandler())

    try:
        init_db()
        init_tracking_system()

    except Exception as e:
        app.logger.error(f"Error during app initialization: {e}")
        raise

    # Register Blueprints
    with app.app_context():
        from .routes import bp as main_blueprint
        app.register_blueprint(main_blueprint)

    return app

def create_app():
    """Initialize the Flask app."""
    app = Flask(__name__)
    app.config['SECRET_KEY'] = os.getenv('SECRET_KEY')
    app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///frostbytectf.db'
    app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False

    db.init_app(app)
    migrate.init_app(app, db)

