info=[
    ("bidisha","maths"),
    ("rumi","science"),
    ("soumya","english"),
    ("sneha","geography"),
    ("tania","english"),
    ("bidisha","science"),
    ("soumya","maths"),


    
]

unique_course=set()
for tup in info:
    unique_course.add(tup[1])
print(unique_course)
    

for name,course in info:
    if (course=="english"):
        print(name) 

dict={}
for name,course in info:
    if (dict.get(name)==None):
        dict.update({name:set()})
        dict[name].add(course)
    else:
        dict[name].add(course)
print(dict)

