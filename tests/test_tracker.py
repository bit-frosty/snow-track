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
    
    def test_asset_movement(self):
        """Test the simulated movement of assets."""
        start_asset_tracking('Leo')  # Simulate movement in background
        time.sleep(6)  # Allow some time for movement
