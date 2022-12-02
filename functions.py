
a=10
b=17
c=sum((a,b))
print(c)

def function1(a,b):
    """This a function which will print average of two number"""
    avg=(a+b)/2
    return(avg)
var=function1(int(input("enter first number")),int(input("enter second number")))
print(var)
print(function1.__doc__)