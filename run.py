# run.py
from tracker import Tracker
from utils import validate_input

def main():
    data = {"username": "john_doe", "age": 30}
    required_fields = ["username", "age"]

    valid, message = validate_input(data, required_fields)
    if valid:
        tracker = Tracker()
        tracker.log_event("INFO", "User data validated successfully.")
    else:
        print(f"Validation failed: {message}")

if __name__ == "__main__":
    main()
