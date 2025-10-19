#function definition
def sum(a,b):#a,b are the parameters
    sum=a+b
    return sum


print(sum(3,5))#a and b are the arguments


#Q.1

#average of 3 numbers

def avg(a,b,c):
    return (a+b+c)/3


print(avg(9,9,18))

#build-in functions

print("bidisha",end=" ") #sep =" "
print("das")#end="/n"

def cal_prod(a=2,b=2):
    prod=a*b
    print(prod)
    return prod

cal_prod()

#Q.2

numbers=[1,2,3,4,5]
def print_len(list):
    print(len(list))

print_len(numbers)

#Q.3
num=[10,20,30,40,50]
def traverse(list):
    for i in list:
        print(i , end=" ")

traverse(num)

#Q.4
def factorial(n):
    fact=1
    for el in range(1,n+1):
        fact=fact*el
    return fact

print(factorial(5))


#Q.5
def converter(usd_rs):
    inr=usd_rs*83
    print(inr)
    return inr

converter(4)

#Q.6

def odd_even(num):
    if num%2==0:
        print("EVEN")
    else:
        print("ODD")   


odd_even(12354678)


#recursion

def show(n):
    if (n==0):
        return
    print(n , end=" ")
    show(n-1)

show(10)    


def fact(n):
    if n==0 or n==1:
        return 1
    else:
        return n * fact(n-1)
    
print(fact(4))    


#Q.7

def calc_sum(n):
    if n==0:
        return 0
    return n + calc_sum(n-1)
    

print(calc_sum(10))

#Q.8
values=[1,2,3,4,5]
def print_list(list,idx):
    if idx==len(list):
        return
    print(list[idx],end=" ")
    print_list(list, idx+1)


print_list(values,0)    


