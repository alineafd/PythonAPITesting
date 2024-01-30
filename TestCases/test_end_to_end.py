import requests
import json
import jsonpath

def test_Add_new_data():
    App_URL = "https://thetestingworldapi.com/api/studentsDetails"
    f = open('C:\\Users\\aline\\OneDrive\\Documentos\\Cursos Udemy\\RequestJson.json', 'r')
    request_json = json.loads(f.read())
    response = requests.post(App_URL, request_json)
    print(response.text)
    id = jsonpath.jsonpath(response.json(), 'id')
    print(id[0])

    tech_api_url = "https://thetestingworldapi.com/api/technicalskills"
    f = open('C:\\Users\\aline\\OneDrive\\Documentos\\Cursos Udemy\\TechDetails.json', 'r')
    request_json = json.loads(f.read())
    request_json['id'] = id[0]
    request_json['stId'] = id[0]
    response = requests.post(tech_api_url, request_json)
    print(response.text)

    add_api_url = "https://thetestingworldapi.com/api/addresses"
    f = open('C:\\Users\\aline\\OneDrive\\Documentos\\Cursos Udemy\\address.json', 'r')
    request_json = json.loads(f.read())
    response = requests.post(add_api_url, request_json)
    print(response.text)

    final_detail = "https://thetestingworldapi.com/api/FinalStudentDetails/"+str(id[0])
    response = requests.get(final_detail)
    print(response.text)