import json

def jsonGen(str):
    if(str != ""):
        return json.loads(str)

def jsonPrint(jsonO):
    return json.dumps(jsonO)

def add_employee(salaries_json, name, salary):
    # Add your code here
    salaryjson2 =  json.loads(salaries_json)
    salaryjson2[name] = salary
    return json.dumps(salaryjson2)

# test code
salaries = '{"Alfred" : 300, "Jane" : 400 }'

new_salaries = add_employee(salaries, "Me", 800)
decoded_salaries = json.loads(new_salaries)
print(decoded_salaries["Alfred"])
print(decoded_salaries["Jane"])
print(decoded_salaries["Me"])
