'''
Created on Sep 24, 2019

@author: CJ
'''
import unittest
import requests
import json

class Test(unittest.TestCase):
    @classmethod
    def setUp (self):
        self.ID = 'cjarrett1'
        self.ID2 = 'INVALID_USER'

    def testValidUser(self):
        api = 'https://api.github.com/users/'+self.ID+'/repos'
        r = requests.get(api)
        self.assertEquals(r.status_code,200)
        
    def testInvalidUser(self):
        api = 'https://api.github.com/users/'+self.ID2+'/repos'
        r = requests.get(api)
        self.assertEquals(r.status_code,404)
    

if __name__ == "__main__":
    unittest.main()