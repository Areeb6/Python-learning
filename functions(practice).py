import math

print("COST OF TENT CALCULATOR\n")
print("Note:\nPLEASE ENTER ALL THE VALUES IN ONE UNIT SO THAT CALCULATION WILL BE ACCURATE. eg:in metres or centimeters or etc\n")
print("Enter details to get area of your cloth int sq.unit")
try:
    r=int(input("Enter radius of tent that you want: "))
    h1=int(input("Enter height of conical part that you want to see in your tent: "))
    h2=int(input("enter the height of cylindrical part that you want to see in your tent: "))
except Exception as e:
    print("PLEASE ENTER NUMERIC VALUES")

def calc(r,h1):
    print({[(h1)^2]+[(r)^2]}^1/2)
calc(r,h1)


