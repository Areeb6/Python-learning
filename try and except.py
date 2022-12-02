num1=(input("Enter first number:\n"))
num2=(input("Enter second number:\n"))
print("sum of both numbers is:")
try:
    print(int(num1)+int(num2))
except Exception as a:
    print(a)
print("hello")
