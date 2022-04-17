# python object to json file.....
import json



x={
    '4': 5, 
    '6': 7, 
    '1': 3, 
    '2': 4
    }


# a=json.dumps(x,sort_keys=True)
# print(a)
# print(type(a))


with open("sortfile.json","w") as f:


    json.dump(x,f,sort_keys=True,indent=2)

    f.close()
