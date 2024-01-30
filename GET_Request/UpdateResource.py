import json

import jsonpath
import requests

#API URL
url = "https://reqres.in/api/users/2"

# Read Input Json File
file = open('C:\\Users\\aline\\OneDrive\\Documentos\\Cursos Udemy\\CreateUser.json')
json_input = file.read()
request_json = json.loads(json_input)

print(request_json)
response = requests.put(url, request_json)

# Validating response code
assert response.status_code == 200

# Parse response content
response_json = json.loads(response.text)
updated_li = jsonpath.jsonpath(response_json, 'updatedAt')
print(updated_li[0])

