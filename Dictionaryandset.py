
my_dict = {
    "key": "value",
    "Name": "Bidisha",
    "Subject": ["python", "C", "Java"],
    "age": 34,
}
print(my_dict)


print(my_dict["Name"])

my_dict["age"]=40
print(my_dict)

# null dictionary
null_dict={}
null_dict["name"]="java"
print(null_dict)

#nested dictionary
student = {
    "name" : "Python",
    "subjects" : {
        "phy" :82,
        "maths" : 90,
        "chem" : 95
    }
}

print(student["subjects"]["maths"])

# dictionary methods
print(len(student)) # number of key value pairs
print(list(student.keys()))
print(list(student.values()))
print(list(student.items()))
print(student.get("name"))

#student.update({"City" : "Kolkata"})
#print(student)

new_dict={"name" :"Java","age":34}
student.update(new_dict)
print(student)


#set in python
collection = {1,2,2,4,5,5,5,"Bidisha","Bidisha"} # duplicate values are ignored in set
print(collection)
print(type(collection))
print(len(collection))

sets={} #empty dictionary
print(type(sets))
group=set() # empty set
print(type(group))
 # set methods

group.add(2)
group.add(1)
group.add(23)
group.add("bidisha")
group.add((2,3,4,5))
print(group) 
group.remove(2)
#group.clear()
#group.pop()
print(group)


set1={1,2,3,4}
set2={3,4,5,6,7}
new_set = set1.union(set2)
common_element=set1.intersection(set2)
print(common_element)
print(new_set)


#Q.1
dict1={
    "cat" :"a small animal",
    "table": ["a piece of furniture" , "lists of facts and figures"]
}

print(dict1)

#Q.2
dict2={"python","java","C++","python","javascript","java","python","java","C++","C"}
print("No. of classroom needed:",len(dict2))


#Q.3
dictionary={}
p=int(input("Enter physics marks: "))
c=int(input("Enter chemistry marks: "))
m=int(input("Enter maths marks: "))
dictionary.update({"phy" :p })
dictionary.update({"chem" : c})
dictionary.update({"math" : m})
print(dictionary)


#q.4
values = {
("int" , 9),    
("float" , 9.0),
}


print(values)


