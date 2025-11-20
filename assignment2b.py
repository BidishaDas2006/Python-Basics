#Q.6
for i in range(1,101):
    if (i%3==0 and i%5==0):
        print(i)



#Q.7

while True:
    n=input("enter a number: ")

    if n=="Quit":
        print("you Quitted")
        break
    num=float(n)
    if num>0:
        print("positive")
        
    else:
        print("negative") 

#Q.8

 
def calculator(a, b, operation):
    match operation:
        case '+':
            return a + b
        case '-':
            return a - b
        case '*':
            return a * b
        case '/':
            return a / b

print(calculator(20, 5, '*'))


#Q.9

def is_prime(n):
    
     
    for i in range(2,n-1):
          if n%i==0:
               print("False")
               break
    else:
        print("True")
               
    
is_prime(7)


#Q.10

number=76
while True:
    n=int(input("enter a number(1-100): "))

    if (number==n):
        print("correct!")
        break


    elif (number>n):
        print("Too low")

    else:
        print("Too high")    










          
    

     
