a = int(input("please add number of line you want to print"))
b = bool(int(input("please add 0 for False and 1 for True")))

def astrstar(a,b):
    if b==True:
        c=1
        while a>=c:
            print(c*"*")
            c=c+1
    else:
        while a>0:
            print(a*"*")
            a=a-1
        
astrstar(a,b)
