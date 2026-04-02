import json
file_path = "data.json"

try:
    with open("data.json", "r") as file:
       data = json.load(file)
except FileNotFoundError or None:
       with open("data.json", "w") as file:
        data =[]
        json.dump(data,file)

def update_storage(new_data):
    with open(file_path,"w") as file:
    #     if type(data) == "dict":
        # data.append(new_data)
        json.dump(new_data,file,indent=4)

def get_bandwith_data():
    with open("data.json", "r") as file:
       data = json.load(file)
       return data