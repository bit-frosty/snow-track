import time
import random
import math
import threading
import logging

# Set up logging for tracking events
logging.basicConfig(level=logging.INFO)
logger = logging.getLogger(__name__)
# tracker.py
import logging

logging.basicConfig(level=logging.INFO, format='%(asctime)s - %(levelname)s - %(message)s')


class Tracker:
    def __init__(self):
        self.events = []

    def log_event(self, event_type: str, details: str) -> None:
        """Logs an event."""
        self.events.append({"type": event_type, "details": details})
        logging.info(f"{event_type}: {details}")

def track_asset(name, location):
    """Simulate tracking an asset's location."""
    print(f"Tracking {name} at {location}")
    # Add a sleep time to simulate real-world tracking (longer delays)
    time.sleep(random.uniform(0.5, 2.0))

def log_event(self, event_type: str, details: str, level: str = "info") -> None:
        """Logs events with different levels."""
        log_message = f"{event_type}: {details}"
        if level == "info":
            logging.info(log_message)
        elif level == "error":
            logging.error(log_message)
        elif level == "warning":
            logging.warning(log_message)
        self.events.append({"type": event_type, "details": details, "level": level})

def simulate_tracking_noise(location):
    """Introduce random noise to the location for realism."""
    # Simulating small variations in location
    noise_x = random.uniform(-0.01, 0.01)
    noise_y = random.uniform(-0.01, 0.01)
    new_location = (location[0] + noise_x, location[1] + noise_y)
    log_event("TRACKING", f"Simulated noise added: X={noise_x}, Y={noise_y}")
    return new_location

def start_asset_tracking(name):
    """Start a separate thread for simulating asset movement."""
    import threading
    tracking_thread = threading.Thread(target=simulate_asset_movement, args=(name,))
    tracking_thread.daemon = True
    tracking_thread.start()

if __name__ == "__main__":
    # Initialize the system
    init_tracking_system()

    # Start tracking a specific asset with a starting location
    asset_name = "Laptop"
    initial_location = (50.0, 50.0)  # Starting coordinates (latitude, longitude)
    start_asset_tracking(asset_name, initial_location)
    
    # Allow the simulation to run for some time (e.g., 10 seconds)
    time.sleep(10)
    print("Asset tracking simulation completed.")
