# test_chordjolt.py
"""
Tests for ChordJolt module.
"""

import unittest
from chordjolt import ChordJolt

class TestChordJolt(unittest.TestCase):
    """Test cases for ChordJolt class."""
    
    def test_initialization(self):
        """Test class initialization."""
        instance = ChordJolt()
        self.assertIsInstance(instance, ChordJolt)
        
    def test_run_method(self):
        """Test the run method."""
        instance = ChordJolt()
        self.assertTrue(instance.run())

if __name__ == "__main__":
    unittest.main()
