#Q.1
user_Name=input("Enter username: ")
password=input("Enter password: ")
if user_Name=="admin" and password=="pass":
    print("You have entered successfully!")

elif (user_Name!="admin"):    
    print("invalid username!!")

else:
    print("Invalid password!!")



#Q.2
n=int(input("enter a number: "))
if n%5==0:
    print("the number is a multiple of 5")
else:
    print("the number is not a multiple of 5")


#Q.3
#Match case  
color=input("enter the color: ")

match color:
    case "Green":
        print("Go")
    case "Red":
        print("stop")
    case "yellow":
        print("Ready")    
    case _:
        print("wrong color!!")    
#Q.4
n=int(input("enter a number: "))
i=1
while i<=10:
    print(n,"*",i,"=" ,n*i)
    i+=1

