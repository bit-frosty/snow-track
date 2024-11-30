import time
import random

def track_asset(name, location):
    """Simulate tracking an asset's location."""
    print(f"Tracking {name} at {location}")
    # Add a sleep time to simulate real-world tracking (longer delays)
    time.sleep(random.uniform(0.5, 2.0))

def init_tracking_system():
    """Simulate initializing the tracking system."""
    print("Initializing the FrostByte tracking system...")
    time.sleep(1)
    print("Tracking system is now operational.")
    # Fake initialization process to mislead players into thinking there's more complexity

def simulate_asset_movement(name):
    """Simulate the movement of an asset (e.g., Leo running around)."""
    directions = ['North', 'South', 'East', 'West']
    while True:
        # Random movement every 5 seconds
        new_location = random.choice(directions)
        track_asset(name, new_location)
        time.sleep(5)

# Start simulation for tracking Leo (in the background)
# In the real application, this would be done asynchronously or in a separate thread
def start_asset_tracking(name):
    """Start a separate thread for simulating asset movement."""
    import threading
    tracking_thread = threading.Thread(target=simulate_asset_movement, args=(name,))
    tracking_thread.daemon = True
    tracking_thread.start()

