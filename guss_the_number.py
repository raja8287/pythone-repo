n=18
i=2
while(i>0):
    i=i-1
    g=int(input("gusse the number"))
    if(g==n):
        print("right gusse")

        break
    elif(g>n):
        print("greater then n")
        continue
    elif(g<n):
        print("less then n")
        continue

if(i>0):
    print("out of turns GAME OVER\n")
else:
    print("CONGRATULATIONS YOU WINS")
