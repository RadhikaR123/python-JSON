import json 
dict={1:2,3:4}
fin=json.dumps(dict)
with open("sortfile.json", "r") as file:
    print(type(json.load(file)))