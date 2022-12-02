list=["harry","Larry","Carry","Marry"]
#not good way#
# print(list[0],list[1],list[2],list[3])

#better way#

for item in list:
    print(item)

#list mein list#

list_=[["a",1],["b",2],["c",3],["d",4],["e",10],["f",20]]

for item in list_:
    print(item)

for item,num in list_:
    print(item,"position in number=",num)

#dictionary#

dict=dict(list_)
print(dict)
for item,num in dict.items():
    print (item,num)

for item,num in dict.items():
    if num<10:
        print(item,num)
for item,num in dict.items():
    if num<4:
        print(item,"is allowed")

listq=["areeb",1,2,34,5,635,5354,"hello","world",231,21.3,4,4,65]
for item in listq:
    if str(item).isnumeric() and item>6:
        print(item)
print(type(listq[0]))