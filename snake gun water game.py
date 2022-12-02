import random

points=0

i=0
while i<11:
    i=i+1

    data=["snake","gun","water"]
    comp=random.choice(data)
    player=input("Enter your choice\n")
    
    print("computer:", comp)
    print("You:", player)
    if comp==player:
        print("TIE\n")
    elif comp=="snake" and player=="gun":
        print("you win\n")
        points=points+1
    elif comp=="gun" and player=="water":
        print("you win\n")
        points=points+1
    elif comp=="water" and player=="snake":
        print("you win\n")
        points=points+1
    else:
        print("you lose\n")

    
print("your points=", points)

if points>5:
    print("YOU WIN")
elif points==5:
    print("TIE")
else:
    print("YOU LOSE")

