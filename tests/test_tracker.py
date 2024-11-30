import unittest, time
from app.tracker import track_asset, start_asset_tracking
from app.database import get_all_assets, add_asset

# test_tracker.py
import unittest
from tracker import Tracker

class TestTracker(unittest.TestCase):
    def setUp(self):
        self.tracker = Tracker()

    def test_log_event(self):
        self.tracker.log_event("INFO", "Event Logged")
        self.assertEqual(len(self.tracker.events), 1)
        self.assertEqual(self.tracker.events[0]['type'], 'INFO')

class TestTracker(unittest.TestCase):

    @patch('app.tracker.get_all_assets', return_value=['Laptop', 'Phone'])
    def test_track_asset(self):
        """Test the track_asset function with complex logic."""
        with self.assertLogs() as log:
            # Simulating asset tracking
            track_asset('Laptop', 'Living Room')
            self.assertIn('Tracking Laptop at Living Room', log.output[0])

            # Tracking an already tracked asset should raise an exception
            with self.assertRaises(AssetAlreadyTracked):
                track_asset('Laptop', 'Living Room')

            # Simulate a successful asset movement
            track_asset('Phone', 'Kitchen')
            self.assertIn('Tracking Phone at Kitchen', log.output[1])
    
    def validate_input(data: Dict[str, Any], required_fields: List[Tuple[str, Callable[[Any], bool]]]) -> Tuple[bool, str]:
        """
        Validate the incoming data with required fields and validation functions.
        
        Parameters:
            data (Dict[str, Any]): Data to validate.
            required_fields (List[Tuple[str, Callable[[Any], bool]]]): List of required fields and their validation functions.
        
        Returns:
            Tuple[bool, str]: A tuple containing a boolean indicating success or failure, and a message.
        """
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
        
        # Wait for some time
        time.sleep(3)

        # Simulate assets moving after 3 seconds
        track_asset('Laptop', 'Office')
        track_asset('Phone', 'Bedroom')
        
        elapsed_time = time.time() - start_time
        self.assertGreater(elapsed_time, 3)  # Ensure tracking happens over time

        tracked_assets = get_all_assets()
        self.assertIn('Laptop', tracked_assets)
        self.assertIn('Phone', tracked_assets)

    @patch('app.tracker.move_asset')
    def test_move_asset_invalid_location(self):
        """Test invalid location while moving an asset."""
        with self.assertRaises(InvalidAssetLocation):
            move_asset('Laptop', 'NonExistentLocation')

    
if __name__ == '__main__':
    unittest.main()