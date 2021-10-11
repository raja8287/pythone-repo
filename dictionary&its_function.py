d1={}# {}=dictonary function
print(type(d1))
#{"entity":"attribut of entity"}
d2={"raja":"roti","nisha":"momos","soni":"dal"}
print(d2)
#it will print entitys attribut and also it is case sensitiv(ex:-"raja"is not equal to "RAJA")
print(d2["raja"])
#we can put enitiy in attribute or dictonary in attribut
d3={"raja":"roti","nisha":"momos","soni":{"wed":"roti","fri":"rice","mon":"dal"}}
print(d3["soni"])
#also we can assess the enitiy's attribute's attrbute
print(d3["soni"]["wed"])
#for assining entity's attribute a anyother attribute
d3["raja"]="momos"
print(d3)
d3["soni"]["wed"]="momos"
print(d3)
#for changing the entity's name only in intiger
d3[12]="wed"
print(d3)
#for removing any entity or entity's attribute
"""del d3["soni"]
print(d3)"""
#copy function
d0=d3.copy()#this is coping the actual list but nothing change in actual list(d3)
del d0[12]
print(d0)
#for updating the entity or attribute by function d3.update()
d3.update({"arav":"chips"})
print(d3)
#for entity printing only
print(d3.keys())


