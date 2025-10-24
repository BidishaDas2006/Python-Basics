#creating a class

class Student:
    
    College_name="ABC college" #class attribute(same for each object present in student class)
    # default constructor
    def __init__(self):
        pass

    #parameterized constructor

    def __init__(self,fullname,marks):
        self.name = fullname #instance attribute(different for each student)
        self.marks=marks
        print("Adding new student in database")

    #methods    

    def welcome(self):
        print("welcome",self.name)    

    def get_marks(self):
        print(self.marks)   

#creation of object(instance)

s1= Student("karan","90")
print(s1.College_name)
print(s1.marks)
print(s1.name)
s1.welcome()
s1.get_marks()

s2= Student("k","34")
print(s2.marks)
print(s2.name)   



class Car:
    color="black"
    Brand="Mercedes"

c1=Car()
print(c1.Brand)
print(c1.color)


#Q.1

class student:
    #static mathod= methods that don't use self parameter(works at class level)

    @staticmethod #decorator
    def hello():
        print("Hi")
    def __init__(self,Name,mark):
        self.name=Name
        self.mark=mark
    def get_average(self):
        sum=0
        for i in self.mark:
           sum+=i
        print("Average is :" , sum/3)


   
        


s1=student("Bidisha",[10,10,10])
print(s1.name)
print(s1.mark)
s1.get_average()
s1.hello()
s1.name="Thor"# we can ditrectly change the attribute value
print(s1.name)


#Abstraction(Hides unnecessary  detais from user)->Hiding the implementation details of a class and only showing essential features to the user.

class Bike:
    def __init__(self):
        self.brk=False
        self.clutch=False
        self.acc=False

    def start(self):
        self.acc=True
        self.clutch=True
        print("Bike started...")


B1=Bike()
B1.start()

#Encapsulation-> wrapping data and function into a single unit(object)


#Q.2

class Account:
    def __init__(self,bal,acc):
        self.balance=bal
        self.account_no=acc



    #debit method
    def debit(self ,amount):
        self.balance-=amount
        print("Rs.=>" ,amount, "was debited" ) 
        print("total balance= ",self.get_balance())  

    #Credit method
    def credit(self,amount):
         self.balance+=amount
         print("Rs.=>" ,amount, "was credited" ) 
         print("total balance= ",self.get_balance()) 

    #check balance

    def  get_balance(self):
        return self.balance

acc1=Account(10000, 123456778)
print(acc1.balance)
print(acc1.account_no) 
acc1.debit(2000) 
acc1.credit(5000)
acc1.credit(2000)
acc1.debit(2500)




