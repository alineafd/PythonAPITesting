import requests
import json
import jsonpath

# API URL
url = "https://reqres.in/users"

# Read Input Json File
file = open('C:\\Users\\aline\\OneDrive\\Documentos\\Cursos Udemy\\CreateUser.json')
json_input = file.read()
request_json = json.loads(json_input)

# Make POST request with json input body
response = requests.post(url, request_json)

print(response.content)
print(response.status_code)

# Parse requests to json format
# response_json = json.loads(response.text)

# id = jsonpath.jsonpath(response_json, 'id')
# print(id[0])