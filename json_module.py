import json

json_str='{"name": "John", "age": 30, "city": "New York"}'

py_obj= json.loads(json_str)
print(py_obj)
print(type(py_obj))

# with open("data.json","r") as f:
#     py_obj=json.load(f)
#     print(py_obj)
#     print(type(py_obj))

