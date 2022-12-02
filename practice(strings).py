str1='hello world'
str2="hello world"
str3="""hello world"""
str4='''hello word'''
print(str1,str2,str3,str4)

print(str1[5])
print(str2[2+2])
#print(str2[2+3.4])#
print(str3[-1])
print(len(str1),len(str2),len(str3),len(str4))

#strings are immutable you cannot change them#
str_="hello"
str__=" world"
print(str_+ str__)
print(str_*3)
print(str_*int(str__))

print('w' not in str_)
print(str_[-1:-6:-2])

# Question 1= do we have to memorise all the function(in-built)
#you have to just memorise a few of them #

name="                                                                                                 areeb of REHMAn             "
name1=name.title()
print(name1)

a=name.count('areeb')
print(a)

print(name.find('areeb'))
 
 #if something not present then it will show -1#
print(name.find('RaE'))
print(name.endswith("areeb"))
print(name.startswith('areeb'))
d=name.isalnum()
print(d)
print(name.lstrip())
print(name.rstrip())
print(name.strip())


str3231="-"
str3232="AREEB"
print(str3231.join(str3232))

h="spring, summer, winter and autmn are some seasons."
z=h.title()
print(z)
print(z.partition("Summer,"))
print(z.partition("Rainy"))
print(h.split("e"))
print(z.split())

#---------*********PRACTICE-TIME*********--------------#


#------program-1-----------------#

main_1=input("Enter a statement:")
sec_1=main_1.count(input("Character To Which You Want To Count:"))
print("NUMBER OF TIMES YOUR CHARACTER APEARS:", sec_1)

input()

#------------program-2------------#

main_2=input("Enter a statement:")
print(main_2.replace("a","*"),main_2.replace("e","*"),main_2.replace("i","*"),main_2.replace("o","*"),main_2.replace("u","*"))

input()

#------------program-3------------#

v=input("Enter a String:")
print(v[::-1])
input()

#------------program-4------------#

s=input("Enter Your Statement:")
print("Original string:",s)
j=s[::-1]
print(j)
input()

#------------program-5------------#

g=input("Enter your string:")
kl=g[::-1]
print("Input is palindrome:",kl==g)
input()

#point to be noted(below)#

add="WZ-1, New Ganga Nagar,New Delhi"
print(add.partition(","))

#-----------------program-6-------------------------#

w=input("Enter a string:")
kl=input("Enter the char to be removed:")
print(w.replace(kl,""))
input()

