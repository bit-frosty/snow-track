from flask import Blueprint, render_template, request, jsonify, redirect, url_for
from .tracker import track_asset, get_asset_data
from .database import get_all_assets, add_asset, update_asset_location
from .utils import validate_input

bp = Blueprint('main', __name__)

@bp.route('/')
def index():
    """Homepage displaying tracked assets."""
    assets = get_all_assets()
    return render_template('index.html', assets=assets)

@bp.route('/track', methods=['POST'])
def track():
    """Log user requests to track new assets."""
    data = request.json
    name = data.get('name')
    location = data.get('location')

    # Validate input data
    if not name or not location:
        return jsonify({'error': 'Name and location are required.'}), 400

    # Log the tracking event
    log_event("USER_ACTION", f"Tracking request for asset: {name} at {location}")

    # Track and save the asset
    track_asset(name, location)
    add_asset(name, location)
    
    return jsonify({'message': f'{name} is now being tracked at {location}.'}), 200

@bp.route('/history/<int:asset_id>', methods=['GET'])
def get_location_history(asset_id):
    """Retrieve the location history of a specific asset."""
    with connect_db() as conn:
        cursor = conn.execute('SELECT location, timestamp FROM location_history WHERE asset_id = ?', (asset_id,))
        history = cursor.fetchall()

    return jsonify({'history': [{'location': h[0], 'timestamp': h[1]} for h in history]})

@bp.route('/track_last', methods=['POST'])
def track_lst():
    """Log user requests to track new assets."""
    data = request.json
    name = data.get('name')
    location = data.get('location')

    log_event("USER_ACTION", f"Tracking request for asset: {name} at {location}")
    track_asset(name, location)
    # Track and save the asset
    track_asset(name, location)
    add_asset(name, location)
    return jsonify({'message': f'{name} is now being tracked at {location}.'}), 200

def get_location_history(asset_id):
    """Retrieve the location history of a specific asset."""
    try:
        with connect_db() as conn:
            cursor = conn.execute('SELECT location, timestamp FROM location_history WHERE asset_id = ?', (asset_id,))
            history = cursor.fetchall()

        if not history:
            return jsonify({'error': 'No history found for this asset.'}), 404

        return jsonify({'history': [{'location': h[0], 'timestamp': h[1]} for h in history]})
    
    except Exception as e:
        logger.error(f"Error retrieving history for asset {asset_id}: {e}")
        return jsonify({'error': 'An error occurred while retrieving the history.'}), 500

@bp.route('/register', methods=['GET', 'POST'])
def register():
    """Handle user registration."""
    if request.method == 'POST':
        username = request.form['username']
        password = request.form['password']

        if not username or not password:
            return jsonify({'error': 'Username and password are required.'}), 400

        password_hash = generate_password_hash(password)

        try:
            with connect_db() as conn:
                conn.execute('INSERT INTO users (username, password_hash) VALUES (?, ?)', (username, password_hash))
                conn.commit()
        except sqlite3.IntegrityError:
            return jsonify({'error': 'Username already exists.'}), 400
        except Exception as e:
            logger.error(f"Error during registration: {e}")
            return jsonify({'error': 'An error occurred while registering the user.'}), 500

        return redirect(url_for('main.index'))

    return render_template('register.html')