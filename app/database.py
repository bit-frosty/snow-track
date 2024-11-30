import sqlite3
import os

DATABASE_FILE = 'frostbytectf.db'

def connect_db():
    """Connect to the SQLite database."""
    return sqlite3.connect(DATABASE_FILE)

def init_db():
    """Initialize the database with the required schema."""
    if not os.path.exists(DATABASE_FILE):
        with connect_db() as conn:
            conn.execute('''
                CREATE TABLE IF NOT EXISTS assets (
                    id INTEGER PRIMARY KEY AUTOINCREMENT,
                    name TEXT NOT NULL,
                    location TEXT NOT NULL,
                    last_seen TEXT NOT NULL DEFAULT CURRENT_TIMESTAMP
                )
            ''')
            conn.commit()

def get_all_assets():
    """Retrieve all tracked assets."""
    with connect_db() as conn:
        cursor = conn.execute('SELECT name, location FROM assets ORDER BY last_seen DESC')
        return cursor.fetchall()

def add_asset(name, location):
    """Add a new asset to the database."""
    with connect_db() as conn:
        conn.execute('INSERT INTO assets (name, location) VALUES (?, ?)', (name, location))
        conn.commit()

def update_asset_location(name, new_location):
    """Update the location of an asset."""
    with connect_db() as conn:
        cursor = conn.execute('UPDATE assets SET location = ? WHERE name = ?', (new_location, name))
        conn.commit()
        return cursor.rowcount > 0
