# f=open("happy.txt")
# print(f.readline())
# print(f.readline())

with open("happy.txt") as f:
    print(f.read())
    print(f.readline())