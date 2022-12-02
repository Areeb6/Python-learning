print("Welcome to the Health Management System")

def get_date_time():
     import datetime
     return datetime.datetime.now()

print("Enter the value 1,2,3 for making file of Harry, Rohan, Hammad respectively.\n")
name=int(input())

if name==1:
    var_1=input("Welcome to the directory of Harry Enter D for updating Diet and E for updating exercise\n") 
    if var_1=="D":
        f=open("Harry_Diet.txt","a")
        y_d=input("Enter the details about Deit\n")
        f.write(str([str(get_date_time())])+"\n")
        f.write(y_d+"\n")
        f.close()
    if var_1=="E":
        f=open("harry_exercise.txt","a")
        y_e=input("Enter the details about Exercise\n")
        f.write(str([str(get_date_time())])+"\n")
        f.write(y_e+"\n")
        f.close()
    
elif name==2:
    var_2=input("Welcome to the directory of Rohan Enter D for updating Diet and E for updating exercise\n") 
    if var_1=="D":
        f=open("Rohan_Diet.txt","a")
        y_d=input("Enter the details about Deit\n")
        f.write(str([str(get_date_time())])+"\n")
        f.write(y_d+"\n")
        f.close()
    if var_1=="E":
        f=open("Rohan_exercise.txt","a")
        y_e=input("Enter the details about Exercise\n")
        f.write(str([str(get_date_time())])+"\n")
        f.write(y_e+"\n")
        f.close()

elif name==3:
    var_1=input("Welcome to the directory of Hammad Enter D for updating Diet and E for updating exercise\n") 
    if var_1=="D":
        f=open("Hammad_Diet.txt","a")
        y_d=input("Enter the details about Deit\n")
        f.write(str([str(get_date_time())])+"\n")
        f.write(y_d+"\n")
        f.close()
    if var_1=="E":
        f=open("hammad_exercise.txt","a")
        y_e=input("Enter the details about Exercise\n")
        f.write(str([str(get_date_time())])+"\n")
        f.write(y_e+"\n")
        f.close()
input()