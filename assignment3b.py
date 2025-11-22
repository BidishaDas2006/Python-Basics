#Q.6
words =["apple","banana","kiwi","cherry","mango"]

dict={}

for val in words:
    dict[val]=len(val)

print(dict)   

#Q.7

str=input("enter a string: ")
print(f"no. of spaces : {str.count(" ")}")

#Q.8
list1 =[1,2,3,4] 
list2 =[4,6,7,8]

set1=set(list1)
set2=set(list2)

if (set1.intersection(set2)==set()):
    print("no common elements")

else:
    print("common elements")    


#Q.9

my_list = [1, 2, 3, 2, 4, 3, 5, 2]

seen = set()
duplicates = set()

for x in my_list:
    if x in seen:
        duplicates.add(x)
    else:
        seen.add(x)
print(duplicates)

#Q.10

str=input("enter a string: ")
set1=set(str)
print(set1)
print(len(set1))



