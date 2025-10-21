#open a file
#read mode

f = open("demo.txt", "r")
data= f.read(5)
print(data)
print(type(data))

#write mode and append mode
f = open("demo.txt", "w")
f.write("I will learn ai and ml.")
f.close()

f = open("demo.txt", "a")
f.write("AI is the future.")
f.close()

f=open("sample.txt","w")

#r+=overwrite at the beginning and for both read and write(no truncate)

f= open("demo.txt","r+")
f.write("She should.")
print(f.read())

#w+ mode -> it deletes all the data that was present in that file(truncate), for both read and write

f= open("demo.txt","w+")
print(f.read())
f.write("Bidisha")

# a+ mode  = write and append .it is used for erite and append(no truncate)

f= open("demo.txt","a+")
print(f.read())
f.write("Bidisha")

#with syntax

 
with open("demo.txt","r") as f:
     print(f.read())

with open("demo.txt","w") as f:
    f.write("new content")    

#deleting a file

import os
os.remove("sample.txt")


#Q.1

f= open("practice.txt","w")
f.write("hi everyone\nwe are learning file I/O\n")
f.write("using java.\nI like programmimg in java.")


with open("practice.txt","r") as f:
    data=f.read()

new_data=data.replace("java","python")    
print(new_data)

#Q.2
def word_search():
 with open("practice.txt","r") as f:
    data=f.read()

    if(data.find("learning") !=0):
        print("Found")
    else:
        print("not found")    

word_search()

#Q.3

def search_for_line():
   word="learning"
   data=True
   line_no=1
   with open("practice.txt","r") as f:
      while data:
         data=f.readline()
         if (word in data):
            print(line_no)
            return
         line_no+=1   

    


search_for_line() 

#Q.4

with open("practice.txt","r") as f:
    data= f.read()
    print(data)

    
    nums=data.split(",")
    print(nums)
    count=1

    for i in nums:
        if(int(i)%2==0):
            count+=1 

          


    print(count)      


