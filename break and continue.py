# i=0
# while (True):
#     if i+1<5:
#         i=i+1
#         continue

#     print(i+1)
#     if i+1==45:
#         break
#     i=i+1

while(True):
    a=int(input("Enter a Number:"))
    if a<=100:
        print("Try Again\n")
    if a>100:
        print("Congratulations! You Won")
        break
print("say ne for next or n for Exit:")
b=input("Enter choice\n")
if b=="n":
    print("See You Soon!")
    quit()
if b=="y":
    print("Medium level")
    while(True):
        a=int(input("Enter a Number:"))
        if a<=1002:
            print("Try Again\n")
            continue
        if a>1002:
            print("Congratulations! You Wons")
        break
print("Want to play again: say ne for next or n for Exit")
a=input("Enter choice\n")
if a=="n":
    print("See You Soon!")
    quit()
if a=="y":
    print("Extreme level")
    while(True):
        a=int(input("Enter a Number:"))
        if a<=1001010010100101010110100101010100100101111111111111111111111110000000001010100101010101010100101010010101010011101010101001010010100101011101001010101010101010101010101101010100101010010100101010101100001110101001010100101010:
            print("Try Again\n")
            continue
        if a>1001010010100101010110100101010100100101111111111111111111111110000000001010100101010101010100101010010101010011101010101001010010100101011101001010101010101010101010101101010100101010010100101010101100001110101001010100101010:
            print("Congratulations! You Wons")
        break
print("Want to play again: say ne for next or n for Exit")
a=input("Enter choice\n")
if a=="n":
    print("See You Soon!")
    quit()
if a=="ne":
    print("CONGO! YOU HAVE COMPLETED THE GAME")
