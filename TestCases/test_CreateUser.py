import requests
import json
import pytest

# API URL
url = "https://reqres.in/api/users"
a = 100

@pytest.fixture
def start_exec():
    global file
    file = open('C:\\Users\\aline\\OneDrive\\Documentos\\Cursos Udemy\\CreateUser.json', 'r')

@pytest.mark.Smoke
def test_create_new_user(start_exec):
    # Read Input Json File
    json_input = file.read()
    request_json = json.loads(json_input)
    # Make POST request with json input body
    response = requests.post(url, request_json)
    assert response.status_code == 201

@pytest.mark.Sanity
def test_create_other_user(start_exec):
    # Read Input Json File
    file = open('C:\\Users\\aline\\OneDrive\\Documentos\\Cursos Udemy\\CreateUser.json', 'r')
    json_input = file.read()
    request_json = json.loads(json_input)
    # Make POST request with json input body
    response = requests.post(url, request_json)
    # response_json = json.loads(response.text)
    # id = jsonpath.jsonpath(response_json, 'id')
    # print(id[0])

