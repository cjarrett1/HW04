'''
Created on Sep 24, 2019

@author: CJ
'''
import unittest
import requests
class Test(unittest.TestCase):
    """Unit Test"""
    @classmethod
    def setUp(cls):
        cls.ID = 'cjarrett1'
        cls.ID2 = 'INVALID_USER'
    def test_validuser(self):
        """Check if user is a valid user"""
        api = 'https://api.github.com/users/'+self.ID+'/repos'
        r_1 = requests.get(api)
        self.assertEqual(r_1.status_code, 200)
    def test_invaliduser(self):
        """Check if user is not valid. Status code should return error."""
        api = 'https://api.github.com/users/'+self.ID2+'/repos'
        r_1 = requests.get(api)
        self.assertEqual(r_1.status_code, 404)
if __name__ == "__main__":
    unittest.main()
