import json

x='{"a":"1+5j","b":2,"c":3,"d":4}'

data=json.loads(x)
print(type(data))
print(data)

for i in data:
    print(type(data[i]))
    if type(data[i])=="<class 'complex'>":
        print(data[i])
    else:
        print("not include complex object...")








