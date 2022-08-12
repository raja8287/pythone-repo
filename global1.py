l=10#this is global variabel

def func1():
    #l=5#local varialble only asscss in local function can't use globaly
   # print(l,"this is the local variabel which only in ittrate in local function")
    global l#for chaging the value of the global variable
    l=l+2
    print(l)

func1()

print(l,"this is the global variabel which has a scope globaly ")
