#f=open("raja.txt","w")#will erase all the content of the .txt file and overwright f.wright("word")

#a=f.write("wright words")
#print(a)
#f.close()
#in append mode
p=open("raja.txt","r+")
print(p.read())
#p.write(" thank u")
print(p.readline())
print(p.tell())
p.close()
#another way to open a file
with open("raja.txt") as f:
    a=f.readline()
    print(a)
    #no need to close the file