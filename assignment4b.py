#Q.6
from abc import ABC, abstractmethod
class Employee:
    @abstractmethod
    def calculate_salary(self):
        pass

class Intern(Employee):
    def calculate_salary(self):
        print("Salary of intern is : 20000")


class FullTimeEmployee(Employee):
    def calculate_salary(self):
        print("Salary of intern is : 80000")

class ContractEmployee(Employee):
    def calculate_salary(self):
        print("Salary of intern is : 50000")        

E1=FullTimeEmployee()
E1.calculate_salary()

C1=ContractEmployee()
C1.calculate_salary()


#Q.7
class Person:
    def __init__(self, name, age=None, address=None):
        self.name = name
        self.age = age
        self.address = address

    def display(self):
        print("Name:", self.name)

        if self.age is not None:
            print("Age:", self.age)

        if self.address is not None:
            print("Address:", self.address)

p1 = Person("Rahul")
p1.display()


p2 = Person("Anjali", 22)
p2.display()


p3 = Person("Amit", 25, "Delhi")
p3.display()            


#Q.8
class player:
    player_count=0
    def __init__(self,name,level):
        self.name=name
        self.level=level

        player.player_count+=1

    def display(self):
        print("Name:", self.name)
        print("Level:", self.level)


p1 = player("Ravi", 5)
p2 = player("Aman", 8)
p3 = player("Sita", 4)

p1.display()
p2.display()
p3.display()

print("Total Players Created:", player.player_count)


#Q.9

class Herbivore:
    def __init__(self,veg):
        self.veg=veg

class Carnivore:
    def __init__(self,meat):
        self.meat=meat

class Omnivore:
    def __init__(self,both):
        self.both=both

class Bear(Herbivore,Carnivore,Omnivore):
    def __init__(self,sound,veg,meat,both):
        super().__init__(veg)
        Carnivore.__init__(self,meat)
        Omnivore.__init__(self,both) 
        self.sound=sound

B1=Bear("Roar!","eats_veg","eats_meat","eats_both") 
print(B1.sound)       
print(B1.veg)
print(B1.meat)
print(B1.both)


