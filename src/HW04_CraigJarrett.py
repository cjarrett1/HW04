'''
Created on Sep 22, 2019

@author: CJ
'''
import requests
import json


def github_user():
    ID = input('Enter Github user:')
    api = 'https://api.github.com/users/' + ID + '/repos'
    r = requests.get(api)
    response = r.json()
    return response

r = github_user()
print(r)