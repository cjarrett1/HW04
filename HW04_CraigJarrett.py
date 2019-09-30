'''
Created on Sep 22, 2019

@author: CJ
'''
import requests

def github_repo(git_id):
    api = 'https://api.github.com/users/' + git_id + '/repos'
    r_1 = requests.get(api)
    response = r_1.json()
    i = 0
    while i < len(response):
        git_data = response[i]
        count = github_commits(git_data['url'] + '/commits')
        print('Repo: '+git_data['name'] + ' || ' + 'Number of commits: '+count)
        i += 1
def github_commits(url):
    commit_count = 0
    api2 = url
    r_2 = requests.get(api2)
    response2 = r_2.json()
    for git_dict in response2:
        git_data = git_dict
        for key in git_data:
            if key == 'commit':
                commit_count += 1
    return str(commit_count)
ID = input('Enter Github user:')
github_repo(ID)
