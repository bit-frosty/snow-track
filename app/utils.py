import random
import logging
from hashlib import sha256
# Set up a logger
logging.basicConfig(
    filename='frostbyte.log',
    level=logging.INFO,
    format='%(asctime)s [%(levelname)s]: %(message)s',
    datefmt='%Y-%m-%d %H:%M:%S'
)

def hash_password(password):
    """Hash passwords using SHA-256."""
    hashed = sha256(password.encode()).hexdigest()
    log_event("SECURITY", "Password hashed for storage")
    return hashed

def verify_password(password, hashed_password):
    """Verify hashed passwords."""
    return hash_password(password) == hashed_password


def log_event(event_type: str, details: Any, level: str = "info") -> None:
    """
    Log events in the application with different levels.
    
    Parameters:
        event_type (str): Type of event (e.g., 'ERROR', 'INFO', 'WARNING').
        details (Any): Additional details about the event.
        level (str): Logging level ('info', 'warning', 'error', etc.).
    """
    log_message = f"{event_type}: {details}"
    if level.lower() == "debug":
        logging.debug(log_message)
    elif level.lower() == "info":
        logging.info(log_message)
    elif level.lower() == "warning":
        logging.warning(log_message)
    elif level.lower() == "error":
        logging.error(log_message)
    elif level.lower() == "critical":
        logging.critical(log_message)
    else:
        logging.info(f"Unknown log level for {event_type}: {details}")

# utils.py
def validate_input(data, required_fields):
    """
    Validate incoming data.
    """
    for field in required_fields:
        if field not in data:
            return False, f"Missing required field: {field}"
    return True, None


def retrieve_secret_key():
    """Retrieve the secret key from a hidden location."""
    # The flag is hidden inside this function in a seemingly irrelevant piece of code.
    secret_key = "FLAG\{F4K3_FL4G\}"
    return secret_key
