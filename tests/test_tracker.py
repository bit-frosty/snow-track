import unittest, time
from app.tracker import track_asset, start_asset_tracking
from app.database import get_all_assets, add_asset

class TestTracker(unittest.TestCase):
    def test_track_asset(self):
        """Test the track_asset function."""
        with self.assertLogs() as log:
            track_asset('Laptop', 'Living Room')
            self.assertIn('Tracking Laptop at Living Room', log.output[0])

    def test_asset_movement(self):
        """Test the simulated movement of assets."""
        start_asset_tracking('Leo')  # Simulate movement in background
        time.sleep(6)  # Allow some time for movement
