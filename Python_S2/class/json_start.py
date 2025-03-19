import json
import requests
# What is a json file
# key:value python-dictionary type file

json_data = {
  "name": "Alice",
  "age": 25,
  "isStudent": True,
  "hobbies": ["reading", "swimming", "coding"],
  "address": {
    "city": "New York",
    "zip": "10001"
  }
}

# to write a file in json format
path2json = "./myjson.json"

with open(path2json, 'w+') as f:
    json.dump(json_data,f,indent=4)

# to open a json file, read a json file as a dict
path = "./myjson.json"

with open(path) as f:
    data = json.load(f) # 

for line in data:
    if data.get(line) == "Alice":
        print(f" her {line} is {data[line]}")
# print(data)


# from a given api to get a json file

response = requests.get("https://jsonplaceholder.typicode.com/users")
print(type(response))
# interpret json data
data = response.json
print(type(data), data)