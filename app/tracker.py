import time
import random
import math
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

def simulate_tracking_noise(location):
    """Introduce random noise to the location for realism."""
    noise = random.uniform(-0.01, 0.01)
    new_location = (location[0] + noise, location[1] + noise)
    log_event("TRACKING", f"Simulated noise added: {noise}")
    return new_location

def track_asset(name, location):
    """Track asset with noise simulation."""
    location_with_noise = simulate_tracking_noise(location)
    print(f"Tracking {name} at {location_with_noise}")
    notify_location_update(name, location_with_noise)


def start_asset_tracking(name):
    """Start a separate thread for simulating asset movement."""
    import threading
    tracking_thread = threading.Thread(target=simulate_asset_movement, args=(name,))
    tracking_thread.daemon = True
    tracking_thread.start()

