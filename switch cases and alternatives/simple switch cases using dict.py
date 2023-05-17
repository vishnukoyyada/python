def sdf(a,b):
    print("first string",a)
    print("second string",b)
def myfun(x):
    y={
        0:"apple",
        1:"banana",
        2:"cat",
        3:"doll",
        4:sdf(m,n)
    }
    return y.get(x)
f=int(input("enter the choosen number for the execution of the function:\n"))
m=input("enter the first string:\n")
n=input("enter the second string:\n")
print(myfun(f))