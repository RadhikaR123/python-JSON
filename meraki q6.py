
import json

x={"a":1,"a":2,"a":3,"a":4,"b":1,"b":2}

print("original keys",x)

with open("rajoriya.json","w") as f:
    json.dump(x,f,indent=2)

with open("rajoriya.json","r") as F:
    b=json.load(F)
    print(b)

