#normal formatting
a=10
b=5
sum=a+b
print("sum is {}".format(sum))


print("language is {}".format("python"))
print("languages are {},{},{}".format("python","java","javascript"))

#index based formatting
print("sum of {1} & {0} is {2}".format(a,b,sum))

#value based formatting
print("variables are {x},{y},{z}".format(x=9,y=90,z=900))


#F-string
a=90
b=80
print(f"sum of {a} & {b} is {a+b}")