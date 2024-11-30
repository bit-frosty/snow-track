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
    """API endpoint to track a new asset."""
    data = request.json
    required_fields = ['name', 'location']

    is_valid, error = validate_input(data, required_fields)
    if not is_valid:
        return jsonify({'error': error}), 400

    name = data.get('name')
    location = data.get('location')

    # Track and save the asset
    track_asset(name, location)
    add_asset(name, location)
    return jsonify({'message': f'{name} is now being tracked at {location}.'}), 200

@bp.route('/register', methods=['GET', 'POST'])
def register():
    """Handle user registration."""
    if request.method == 'POST':
        username = request.form['username']
        password = request.form['password']
        password_hash = generate_password_hash(password)

        try:
            with connect_db() as conn:
                conn.execute('INSERT INTO users (username, password_hash) VALUES (?, ?)', (username, password_hash))
                conn.commit()
        except sqlite3.IntegrityError:
            return jsonify({'error': 'Username already exists.'}), 400

        return redirect(url_for('main.index'))
    return render_template('register.html')


@bp.route('/update_location', methods=['POST'])
def update_location():
    """Update the location of an already tracked asset."""
    data = request.json
    required_fields = ['name', 'new_location']

    is_valid, error = validate_input(data, required_fields)
    if not is_valid:
        return jsonify({'error': error}), 400

    name = data.get('name')
    new_location = data.get('new_location')

    # Update the asset's location
    updated = update_asset_location(name, new_location)
    if updated:
        return jsonify({'message': f'{name} location updated to {new_location}.'}), 200
    else:
        return jsonify({'error': f'{name} not found.'}), 404
