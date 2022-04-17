import json
file="text.txt"
dic={}

with open(file) as f:                                #read file
    for d in f:
        key,desc=d.strip().split(None,1)                    #read line from file
        dic[key]=desc.strip()
ourfile=open("output.json","w")
json.dump(dic,ourfile)
ourfile.close()






