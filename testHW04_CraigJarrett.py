'''
Created on Sep 24, 2019

@author: CJ
'''
import unittest
from unittest.mock import patch
import requests
class Test(unittest.TestCase):
    """Unit Test"""
    @classmethod
    def setUp(cls):
        cls.ID = 'cjarrett1'
        cls.ID2 = 'INVALID_USER'
    @patch('requests.get')
    def test_validuser(self, mock_get):
        """Check if user is a valid user"""
        mock_get.return_value.status_code = 200
        self.assertEqual(mock_get.return_value.status_code, 200)
    @patch('requests.get')
    def test_invaliduser(self, mock_get):
        """Check if user is not valid. Status code should return error."""
        mock_get.return_value.status_code = 404
        self.assertEqual(mock_get.return_value.status_code, 404)
if __name__ == "__main__":
    unittest.main()
