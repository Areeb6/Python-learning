i=37
nt=0
nt=nt+1
x=0
while 0<nt<=5:
    nt=nt+1
    p=int(input("Enter a number: "))
    if p<i:
        print("You entered smaller number")
    elif p>i:
        print("You entered larger number")
    elif p==i:
        print("HURRAY! You Won.","in",nt-1,"turns")
        break
    while nt==6:
        print("game over")
        break
