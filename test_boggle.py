import unittest
import boggle

class TestBoggle(unittest.TestCase):
    """
    Our test suite for Boggle Solver
    """
    
    def can_create_an_empty_grid(self):
        """
        Test to see if we can create an empty grid
        """
        grid = boggle.make_grid(0,0)
        self.assertEqual(len(grid), 0)