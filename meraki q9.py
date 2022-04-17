import json


x={
    "shopping_list":
        { 
            "chaco":"15",
            "Biscuits":"50",
            "Diary_milk":"30",
            "ice_cream":"20",
        } 
}

with open("shopping.json","w") as f:
    json.dump(x,f,indent=2)


with open("shopping.json","r") as fn:
    data=json.load(fn)
    print(data)
    
item=input("which item you want to buy :")
for k,v in data.items():
    for k1,v1 in v.items():
        if item==k1:
            qnt=int(input("how much quantity you want:"))
            v1=int(v1)-qnt
        data[k][k1]=v1

print(data)

data["shopping_list"]["biscuit 20-20"]="50"
data["shopping_list"]["namkeen"]="20"

print(data)

with open("shopping.json","w") as f:
    json.dump(data,f,indent=2)


