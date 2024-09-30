import json


with open("data.json", "r") as f:
    data = json.load(f)

genre = "1"

for key, value in data.items():
    for item in value.values():
        if item == genre:
            print(key)
    

# todo search for starting letters
def autoComplete(a):
   
   for key, value in data.items():
    for item in value.values():
        if item == a:
            print(item) 

# todo
def search():
    pass


autoComplete("Cs2")