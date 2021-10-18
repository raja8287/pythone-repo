f=open("raja.txt","w")#will erase all the content of the .txt file and overwright f.wright("word")

a=f.write("wright words")
print(a)
f.close()
#in append mode
p=open("raja.txt","r+")
print(p.read())
p.write(" thank u")
