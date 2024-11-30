# run.py
from tracker import Tracker
from utils import validate_input, log_event

def main():
    data = {"username": "john_doe", "age": 30}
    required_fields = [("username", str), ("age", int)]

    valid, message = validate_input(data, required_fields)
    if valid:
        tracker = Tracker()
        tracker.log_event("INFO", "User data validated successfully.", level="info")
    else:
        log_event("ERROR", message, level="error")

if __name__ == "__main__":
    main()
