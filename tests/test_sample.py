import unittest
from src.utils import greet

class TestUtils(unittest.TestCase):
    def test_greet(self):
        self.assertEqual(greet("AI"), "Hello, AI!")

if __name__ == "__main__":
    unittest.main()
