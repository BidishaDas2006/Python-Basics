#Q.1

def average(a,b,c):
    average=(a+b+c)/3
    return average
print(average(5,10,15))

#Q.2
avg=lambda a,b,c: (a+b+c)/3
print(avg(5,10,15))

#Q.3

def factorial(n):

    n=int(input("enter a number to find factorial: "))
    fact=1
    for i in range(1,n+1):
        fact*=i
    print("factorial of",n,"is:",fact)   

factorial(6)     