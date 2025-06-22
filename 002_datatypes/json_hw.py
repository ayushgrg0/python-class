'''
Q1. Convert JSON Data to Python Object
'''

import json

json_data = '{ "name" : "Ayush", "age": 19, "location": "lekhnath"}'

print(type(json_data))

print(json_data)

py_data = json.loads(json_data)

print(type(py_data))

print(py_data)


'''
Q2. Convert Python Object to JSON Data
'''
py_obj = {
    "City": "KTM",
    "Population": "8,45,767",
    "altitude": "1,324 meters"
}

print(type(py_obj))

print(py_obj)

json_obj = json.dumps(py_obj)

print(type(json_obj))

print(json_obj)


'''
Q3. Convert Python Objects into JSON Strings
'''
python_dict = {"name": "ram", "age": 20, "location": "Birgunj"}

print(type(python_dict))

python_list = ["Red", "Green", "Black"]

print(type(python_list))

json_dict = json.dumps(python_dict)

json_list = json.dumps(python_list)

print("json dict : ", json_dict)
print(type(json_dict))

print("jason list : ", json_list)
print(type(json_list))
