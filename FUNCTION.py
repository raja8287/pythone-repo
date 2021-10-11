def function1():
    print("fuction:function1 is called")

print(function1())#None because function do't give any value due to return is not in the end of the function"""
def jod(a,b):
    print("this is function :jod")
    return a+b

print(jod(2,3))

def fun2():
    """This is calling function fun2"""#this is docstring
    print("this is function:fun2")
    return

print(fun2.__doc__)