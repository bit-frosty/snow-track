import unittest, time
from app.tracker import track_asset, start_asset_tracking
from app.database import get_all_assets, add_asset

# test_tracker.py
import unittest
from tracker import Tracker

class TestTracker_new(unittest.TestCase):
    def setUp(self):
        self.tracker = Tracker()

    data = Tracker()
    def test_input_validation_success(self):
        data = {"username": "john_doe", "age": 30}
        required_fields = [("username", str), ("age", int)]
        valid, message = validate_input(data, required_fields)
        self.assertTrue(valid)
        self.assertEqual(message, "Validation passed.")

    def test_input_validation_failure(self):
        data = {"username": "john_doe", "age": "30"}  # age should be an int
        required_fields = [("username", str), ("age", int)]
        valid, message = validate_input(data, required_fields)
        self.assertFalse(valid)
        self.assertIn("Field age should be of type int", message)
    

class TestTracker(unittest.TestCase):

    def setUp(self):
        self.tracker = Tracker()

    @patch('app.tracker.get_all_assets', return_value=['Laptop', 'Phone'])
    def test_track_asset(self):
        """Test the track_asset function with complex logic."""
        with self.assertLogs() as log:
            # Simulating asset tracking
            track_asset('Laptop', 'Living Room')
            self.assertIn('Tracking Laptop at Living Room', log.output[0])

    def test_log_event_info(self):
        self.tracker.log_event("INFO", "Information event", level="info")
        self.assertEqual(len(self.tracker.events), 1)
        self.assertEqual(self.tracker.events[0]['level'], 'info')

    def test_log_event_error(self):
        self.tracker.log_event("ERROR", "Error event", level="error")
        self.assertEqual(len(self.tracker.events), 2)
        self.assertEqual(self.tracker.events[1]['level'], 'error')


    def validate_input(data: Dict[str, Any], required_fields: List[Tuple[str, Callable[[Any], bool]]]) -> Tuple[bool, str]:
        for field, validator in required_fields:
            if field not in data:
                return False, f"Missing required field: {field}"
            if not validator(data[field]):
                return False, f"Field validation failed for: {field} (value: {data[field]})"
        return True, "All fields validated successfully."
    
    @patch('app.tracker.get_all_assets')
    def test_edge_case_asset_not_found(self):
        """Test edge case when asset is not found in the tracking list."""
        with self.assertRaises(AssetNotFound):
            track_asset('NonExistentAsset', 'Living Room')
    
    def test_log_event(self):
        self.tracker.log_event("INFO", "Event Logged")
        self.assertEqual(len(self.tracker.events), 1)
        self.assertEqual(self.tracker.events[0]['type'], 'INFO')

    @patch('app.tracker.get_all_assets')
    def test_asset_tracking_time(self):
        """Test asset tracking duration and movement logic."""
        track_asset('Laptop', 'Living Room')
        track_asset('Phone', 'Kitchen')
        time.sleep(3)

    def test_asset_tracking_with_multiple_updates(self):
        """Test scenario where multiple updates occur to the same asset in quick succession."""
        track_asset('Laptop', 'Living Room')
        track_asset('Laptop', 'Kitchen')  # Update asset's location quickly
        track_asset('Laptop', 'Bedroom')  # Another location update

        # Check the asset's final location
        tracked_assets = get_all_assets()
        self.assertIn('Laptop', tracked_assets)
        self.assertEqual(tracked_assets['Laptop'], 'Bedroom')
    
        # Simulate assets moving after 3 seconds
        track_asset('Laptop', 'Office')
        track_asset('Phone', 'Bedroom')
        
        elapsed_time = time.time() - start_time
        self.assertGreater(elapsed_time, 3)  # Ensure tracking happens over time

        tracked_assets = get_all_assets()
        self.assertIn('Laptop', tracked_assets)
        self.assertIn('Phone', tracked_assets)

    def test_asset_tracking_time(self):
        """Test asset tracking duration and movement logic."""
        start_time = time.time()

        # Start tracking assets
        track_asset('Laptop', 'Living Room')
        track_asset('Phone', 'Kitchen')

    @patch('app.tracker.move_asset')
    def test_move_asset_invalid_location(self):
        """Test invalid location while moving an asset."""
        with self.assertRaises(InvalidAssetLocation):
            move_asset('Laptop', 'NonExistentLocation')

    
if __name__ == '__main__':
    unittest.main()