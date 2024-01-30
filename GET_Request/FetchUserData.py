import json

import jsonpath
import requests

#API URL

url = "https://reqres.in/api/users?page=2"

# Send Get Request
response = requests.get(url)
print(response)

# Display response content
print(response.content)
print(response.headers)

# Validate status code
print(response.status_code)

assert response.status_code == 200

# Fetch response header
print(response.headers)
print(response.headers.get('Date'))
print(response.headers.get('Server'))

# Fetch Cookies
print(response.cookies)

#Fetch Enconding
print(response.encoding)

print(response.elapsed)

print(response.content)

# parse response to json path
json_response = json.loads(response.text)
print(json_response)

# fetch value using  json path
pages = jsonpath.jsonpath(json_response, 'total_pages')
print(pages[0])
assert pages[0] == 2

# Fetch value using json path
for i in range(0,3):
    first_name = jsonpath.jsonpath(json_response, 'data['+str(i)+'].first_name')
    print(first_name[0])