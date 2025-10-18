count = 1
while count<=5:
    print("Hello, World!")
    count+=1
print(count)

i=1
while i<=20:
    print("Bidisha" , i)
    i+=1


i=1
while i<=5:
    print(i)
    i+=1

#Q.1

i=1
while i<=100:
    print(i)
    i+=1

#Q.2
j=100
while j>=1:
    print(j)
    j-=1

#Q.3

n=int(input("enter the number: "))

i=1
while i<=10:
    print(n*i)
    i+=1


#Q.4

list=[1,4,9,16,25,36,49,64,81,100]
i=0
while i<=9:
    print(list[i])
    i+=1


#Q.5

tup=(1,4,9,16,25,36,49,64,81,100)

x=49
i=0
while i<len(tup):
    if tup[i]==x:
        print("the number is found at index: ",i)
        break
    i+=1

#for loops

nums=[1,2,3,4]
for val in nums:
    print(val)

tuple=(1,2,3,4,5,6)
for num in tuple:
    print(num)


str="Bidishadas2006"    
for char in str:
    print(char)
else:
    print("loop is ended")

#Q.6
numbers=[1,4,9,16,25,36,49,64,81,100]
for value in numbers:
    print(value)

#Q.7

tuple1=(1,4,9,16,25,36,49,64,81,100)
x=36
for num1 in tuple1:
    if num1==x:
        print("the number is found at index: ",tuple1.index(num1))
        break
else:
    print("the number is not found")

    
#range functions


for i in range(2,100,2):

    print(i)

#Q.8
for i in range(1,101):
    print(i)

 #Q.9
n=int(input("enter the number: "))
for i in range(n,n*11,n):
    print(i)

#pass statement

for i in range(11):
     pass      

#Q.10
i=1
sum=0
while i<=100:
    sum+=i
    i+=1
print("the sum is: ",sum) 


#Q.11
fact=1
n=6
for i in range(1,n+1):
    fact*=i
print("the factorial is: ",fact)
