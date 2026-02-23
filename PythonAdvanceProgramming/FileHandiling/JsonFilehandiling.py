import json
with open("C://Users//priya//PycharmProjects//PythonAdvanceProgramming//Dataformats//employee.json", 'r') as file:
     data = json.load(file)

print(data)
print(data["name"])

with open("C://Users//priya//PycharmProjects//PythonAdvanceProgramming//Dataformats//nestedjson.json", 'r') as file:
    data = json.load(file)
email= data["user"]["profile"]["email"]
print(email)

# writing to json file - dump method()
data={
    "name": "Harsha",
  "role": "Tester",
  "experience": 5,
  "skills": ["Python", "Automation", "API"]
}
with open("C://Users//priya//PycharmProjects//PythonAdvanceProgramming//Dataformats//writejson.json", 'w') as file:
    json.dump(data,file)

#update or modify the jason file
#read the json file
#modify the data
#write it back to the file
with open("C://Users//priya//PycharmProjects//PythonAdvanceProgramming//Dataformats//updatejson.json", 'r') as file:
    data = json.load(file)
#update the value
data["experience"] = 6
with open("C://Users//priya//PycharmProjects//PythonAdvanceProgramming//Dataformats//updatejson.json", 'w') as file:
    json.dump(data,file, indent =4)


