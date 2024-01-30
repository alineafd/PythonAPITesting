import jsonpath
import pytest
import requests
import json

@pytest.mark.Smoke
def test_fetch_user_details():
    url = "https://reqres.in/api/users?page=2"
    response = requests.get(url)
    json_response = json.loads(response.text)
    for i in range(0, 3):
        first_name = jsonpath.jsonpath(json_response, 'data[' + str(i) + '].first_name')
        print((first_name[0]))