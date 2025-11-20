#Q.1
salary =int(input("Enter your salary: "))
 
if (salary<30000):
    print("your tax rate is 5%")
elif(salary>=30000 and salary<=70000):
    print("your tax rate is 15%") 

else:
    print("your tax rate is 25%")


#Q.2

def even(a,b):
    for i in range(a,b+1):
        if i%2==0:
            print(i)


even(1,20)

#Q.3


def print_digit(n):
    rev=0
    temp=n

    while temp>0:
        rev=rev*10 +temp%10
        temp//=10

    while rev>0:
        print(rev%10) 
        rev//=10   


          
print_digit(2345)          

#Q.4

def digit_count(n):
    count=0
    while n>0:
        n%10
        
        count+=1
        n//=10
    print(count)

digit_count(12345)  


#Q.5

def sum_of_digits(n):
    sum=0
    while n>0:
        sum+=n%10
        n//=10
    print("sum of the digits: ",sum)    


sum_of_digits(1234)


