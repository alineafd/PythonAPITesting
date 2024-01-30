import requests
import json
import jsonpath
import openpyxl
from DataDriven import Library

def test_add_multiple_students():
    # API
    API_URL = "https://thetestingworldapi.com/api/studentsDetails"
    f = open("C:\\Users\\aline\\OneDrive\\Documentos\\Cursos Udemy\\AddStudent.json", "r")
    json_request = json.loads(f.read())

    obj = Library.Common("C:\\Users\\aline\\OneDrive\\Documentos\\Cursos Udemy\\TestData.xlsx", "Plan1")
    col = obj.fetch_column_count()
    row = obj.fetch_row_count()
    keyList = obj.fetch_key_names()

    for i in range(2, row+1):
        update_json_request = obj.update_request_with_data(i, json_request, keyList)
        response = requests.post(API_URL, update_json_request)
        print(response)
