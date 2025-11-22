#Q.1

word=input("enter a string: ")

rev=""
for i in word:
    rev=rev+i

if word==rev:
    print(f"{word} is a palindrome.")
else:
     print(f"{word} is not a palindrome.") 


#Q.2


def average():
    num=[1,2,3,4,5]

    sum=0
    for i in num:
        sum+=i
    avg=sum/len(num)
    print(int(avg))

average()    
        

#Q.3

list1=[]
n=int(input("enter how many number:"))

for val in range(n):
    val=int(input("enter a number: "))
    list1.append(val)

print(f"list no.1 is {list1}")


list2=[]

for val in range(n):
    val=int(input("enter a number: "))
    list2.append(val)

print(f"list no.2 is {list2}")


result=list1 + list2
print(result)

result.sort()
print(result)

#Q.4
tup=(2,3,56,67,90,22,4,31,30,7,8)
tup_odd=()
tup_even=()

for i in tup:
    if (i%2==0):
        tup_even+=(i,)
    else:
        tup_odd+=(i,)    

print(f"odd tuple is {tup_odd}")
print(f"even tuple is {tup_even}")

#Q.5

students = {}

while True:
    print("\nA - Add a student")
    print("B - Update marks")
    print("C - Search for a student")
    print("D - Display all students and marks")
    print("E - Exit")

    choice = input("Enter your choice: ").upper()

    if choice == 'A':
        name = input("Enter student name: ")
        marks = int(input("Enter marks: "))
        students[name] = marks
        print("Student added!")

    elif choice == 'B':
        name = input("Enter student name to update: ")
        if name in students:
            marks = int(input("Enter new marks: "))
            students[name] = marks
            print("Marks updated!")
        else:
            print("Student not found!")

    elif choice == 'C':
        name = input("Enter student name to search: ")
        if name in students:
            print(f"{name} = {students[name]}")
        else:
            print("Student not found!")

    elif choice == 'D':
        if len(students) == 0:
            print("No students in the dictionary.")
        else:
            for name, marks in students.items():
                print(f"{name} : {marks}")

    

    else:
        print("Invalid choice! Please enter A/B/C/D.")








