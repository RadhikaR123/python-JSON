import json

li1=["neelam","programmer","24","2400"]
li2=["komal","traner","24","20000"]
li3=["anuradha","hr","25","40000"]
li4=["abhishek","manager","29","23000"]

main_list=["name","designation","age","salary"]

dic={}
dic1={}
dic2={}
dic3={}
main_dic={}

i=0
while i<len(li1):
    j=0
    while j<=i:
        dic.update({main_list[i]:li1[j]})
        dic1.update({main_list[i]:li2[j]})
        dic2.update({main_list[i]:li3[j]})
        dic3.update({main_list[i]:li4[j]})
        j+=1
    i+=1


main_dic.update({"em1":dic,"em2":dic1,"em3":dic2,"em4":dic3})
print(main_dic)


with open("mainfile.json","w") as f:
    json.dump(main_dic,f,indent=2)


