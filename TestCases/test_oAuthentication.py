import json
import requests
import jsonpath

def test_oauth_api():
    token_url = 'http://thetestingworldapi.com/Token'
    data = {'grant_type':'password', 'username':'admin', 'password':''}
    response = requests.post(token_url, data)
    print(response.text)
    API_URL = 'http://thetestingworldapi.com/api/StDetails/1104'
    response = requests.get(API_URL)
    print(response.text)