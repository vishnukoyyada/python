def add(a,b):
    x=a+b
    return x
def sub(a,b):
    x=a-b
    return x
def mul(a,b):
    x=a*b
    return x
def divi(a,b):
    x=a//b
    return x
def myfun(x):
    switcher={
        0:add(l,m),
        1:sub(l,m),
        2:mul(l,m),
        3:divi(l,m)
    }
    return switcher.get(x,"please choose correct option:\n")
    #if we choose the wrong number like 4 or 5 then it will print 'please choose correct option'
l=int(input("enter the first number:\n"))
m=int(input("enter the second number:\n"))
#l,m are arguments which are the values need to be assigned at the run time for the parameters  a,b
n=int(input("enter the number in between 0 and 3:\n"))
#n is the argument and x is the parameter for the myfun 
print(myfun(n))