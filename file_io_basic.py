#file io basic
"""
"r"-open file for readig-default
"w"-open a file for writing
"x"-creates file if not exists
"a"-add more content to a file
"t"-text mode
"b"-binary mode
"+"-read and write
"""
f=open("raja.txt")#file opening command
#content=f.read()#read only
#print(content)#printing the file content
for line in f:
    print(line)
f.close()

