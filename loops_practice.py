#q.1
i=1
while i<=10:
    if i%2==0:
        i+=1
        continue
    print(i)
    i+=2
#Q.2
#counts numbdser of i in the word

word="artificial intelligence"

count=0
for char in word:
    if (char=='i'):
        count += 1
print(count)


#Q.3
#print vowel count of a string

word="artificial"
count=0
for i in word:
    if (i=='a' or i=='e' or i=='i' or i=='o' or i=='u'):
        count+=1
print(count)   


#Q.4
#print sum of first N natural numbers

n=int(input("enter a number: "))
sum=0
for i in range(n+1):
    sum+=i
print("sum of first", n,"natural number : ", sum)    

    
   

