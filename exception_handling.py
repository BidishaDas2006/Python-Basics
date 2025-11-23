try:
    x=int(input("enter a number: "))
    ans=10/x

except ZeroDivisionError:
    print("zero is not allowed")

except ValueError:
    print("Invalid input")    

else:
    print(f"the answer is {ans}") 

finally:
    print("end of program")       



