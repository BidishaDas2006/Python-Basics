sq=[i*i for i in range(1,11)]
print(sq)

nums=[-1,-2,-3,4,5,-9,9]
positive=[0 if val<0 else val for val in nums]
print(positive)


words=["hello","world","python"]
words=[val.upper() for val in words]
print(words)