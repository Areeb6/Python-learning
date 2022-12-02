i=10 #global var

def hello(i):
    print(i)
hello(i)

print(i)

#local var

def hello2(i):
    a=2 #local var
    print(a)
hello2(i)
# print(a) #error ayega


l = 10 # Global

def function1(n):
     l = 5 #Local
     m = 8 #Local
     global l
     l = l + 45
     print(l, m)
     print(n, "I have printed")
function1("This is me")
# print(m) error dega