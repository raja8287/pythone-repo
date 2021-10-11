"""i=0
while(True):
    if i<10:
        i=i+1
        continue
    i=i+1
    if(i==20):
        break
    print(i)"""

while(True):
        n=int(input("enter the value\n"))
        if n<100 and n>10:
            print(n,":is in range\n")
            continue
        else:
            print("try again\n")
            break

