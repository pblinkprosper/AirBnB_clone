#!/usr/bin/python3
"""Unittest for models/console.py"""
import unittest
import console
from io import StringIO


class TestConsole(unittest.TestCase):
    """Defining the TestConsole class"""

    def test_add(self):
        self.assertEqual(console.add(2, 3), 5)
    def test_subtract(self):
        self.assertEqual(console.subtract(5, 2), 3)
    def test_multiply(self):
        self.assertEqual(console.multiply(2, 3), 6)
    def test_divide(self):
        self.assertEqual(console.divide(6, 3), 2)

with patch('sys.stdout', new=StringIO()) as f:
    HBNBCommand().onecmd("help show")

if __name__ == '__main__':
    unittest.main()
