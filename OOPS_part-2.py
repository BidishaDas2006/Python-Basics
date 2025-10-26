#Del keyword
# class student:
#      def __init__(self,name):
#           self.name=name


# s1=student("Bidisha")
# print(s1.name)
      


#private and public attribute

class account:
     def __init__(self,acc_no,acc_pass):
          self.Accountnumber=acc_no
          self.__password=acc_pass #(priivate)

     def get_pass(self):
         print(self.__password)      

acc1=account("12345", "abcd")
print(acc1.Accountnumber)
print(acc1.get_pass())
# print(acc1.__password)


class person:
     __name="abcd" #private

     def __hello(self):
          print("hi")

     def welcome(self):#this is accessable outside the class in this way
          self.__hello()


p1=person()
#print(p1.__name)  
print(p1.welcome()) 


#inheritance

class Car:
     def __init__(self,type):
          self.type=type

     @staticmethod
     def start():
          print("Car started..")

     @staticmethod
     def stop():
          
          print("Car stopped..")     

class ToyotaCar(Car):#single inheritance
     def __init__(self,name,type):
          super().__init__(type)
          self.fullname=name
          super().start()

class Fortuner(ToyotaCar):#multilevel inheritance
     def __init__(self,brand):
          self.brand=brand





car1=ToyotaCar("Fortuner","electric") 
# car2=ToyotaCar("Prius")         
print(car1.type)
#print(car1.fullname)
# print(car1.start())

# car1=Fortuner("abcdef")

# print(car1.brand)
# print(car1.type)
# print(car1.stop())



#multiple inheritance

class A:
     varA="welcome to class A"

class B:
      varB="welcome to class B"   



class C(A,B):
     varC="welcome to class C"


C1=C()
print(C1.varC)
print(C1.varA)
print(C1.varB)


class person:
     name="Bidisha"

     # def changeName(self,name):
     #      self.__class__.name="xyz"
          #self.__class__.name /person.name

     @classmethod  #used to change class attributes
     def changeName(cls,name) :
       cls.name=name 

p1=person()
p1.changeName("Rahul Kumar") 
print(p1.name)
print(person.name) 





#@property
class student:
     def __init__(self,phy,chem,math):
          self.phy=phy
          self.chem=chem
          self.math=math
          
     @property #it uses the method as a property
     def percentage(self):
            return str((self.phy+self.chem+self.math)/3) +"%"   

stu1=student(98,68,70)
print(stu1.percentage)

stu1.phy=86
print(stu1.phy)
print(stu1.percentage)



#polymorphism-> Operator overloading
#add two complex number

class Complex:
     def __init__(self,real,img):
          self.real=real
          self.img=img

     def printNumber(self):
          print(self.real,"i +",self.img,"j")

     def __add__(self,Com3):#dunder Function
          newreal=self.real+Com3.real
          newimg=self.img+Com3.img
          return Complex(newreal,newimg)

     def __sub__(self,Com3):
          newreal=self.real-Com3.real
          newimg=self.img-Com3.img
          return Complex(newreal,newimg)     


Com1=Complex(1,3)
Com1.printNumber()

Com2=Complex(23,9)
Com2.printNumber()
Com3=Com1-Com2
Com3.printNumber()


#Q.1
class Circle:

     def __init__(self,radius):
          self.radius=radius

     def Area(self):
          
          print("The Area of the circle: ",3.14*self.radius **2)     


     def periMeter(self):
          print("The perimeter of the circle: ",2*3.14*self.radius) 



C1=Circle(2)
print(C1.radius)
C1.Area()
C1.periMeter()


#Q.2
class Employee:
     def __init__(self,role,dept,sal):
          self.role=role
          self.dept=dept
          self.sal=sal


     def showDetails(self):
          print("the Roll of the employee: ",self.role,"\n","the department of the employee: ",self.dept,"\n","the department of the employee: ",self.sal )     




class Engineer(Employee):
     def __init__(self,name,age):
          self.name=name
          self.age=age
          super().__init__("engineer" ,"IT","70,000")


Eng1=Engineer("Rahul",36)
Eng1.showDetails()


#Q.3

class Order:
      def __init__(self,item,price):
           self.item=item
           self.price=price

      def __gt__(self,ord1):
           return self.price>ord1.price
                

ord1=Order("Tea",20)
ord2=Order("Coffee",40)
print(ord2>ord1)

