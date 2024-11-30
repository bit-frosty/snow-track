import unittest, time
from app.tracker import track_asset, start_asset_tracking
from app.database import get_all_assets, add_asset


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


def test_multiple_asset_tracking(self):
        """Test multiple assets tracking and stop asset tracking."""
        assets = ['Laptop', 'Phone', 'Tablet']

        for asset in assets:
            track_asset(asset, 'Living Room')
        
        # Check if assets are tracked
        tracked_assets = get_all_assets()
        self.assertIn('Laptop', tracked_assets)
        self.assertIn('Phone', tracked_assets)
        self.assertIn('Tablet', tracked_assets)

        # Simulate stopping asset tracking
        stop_asset_tracking('Phone')
        tracked_assets_after_stop = get_all_assets()
        self.assertNotIn('Phone', tracked_assets_after_stop)

    @patch('app.tracker.get_all_assets')
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

    @patch('app.tracker.get_all_assets')
    def test_edge_case_asset_not_found(self):
        """Test edge case when asset is not found in the tracking list."""
        with self.assertRaises(AssetNotFound):
            track_asset('NonExistentAsset', 'Living Room')

if __name__ == '__main__':
    unittest.main()