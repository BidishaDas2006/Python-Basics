#Q.4

class shape:
    def area(self):
        pass

class Circle(shape):
    def __init__(self,radius):
        self.radius=radius
    def area(self):
        return 3.14* self.radius * self.radius  

class   rectangle(shape):
    def __init__(self,length,breadth):
        self.length = length
        self.breadth = breadth

    def area(self):
        return self.length*self.breadth


class triangle(shape) :
    def __init__(self,base,height):
        self.base = base
        self.height = height

    def area(self):
        return 0.5 * self.base * self.height



c = Circle(5)
r = rectangle(4, 6)
t = triangle(10, 3)


print(c.area())
print(r.area())
print(t.area())



#Q.5

class Vehicle:
    def __init__(self,brand,model):
        self.brand=brand
        self.model=model
    def display(self):
        print(f"Vehicle -> Brand: {self.brand}, Model: {self.model}")    

class Car(Vehicle):
    def __init__(self, brand, model,seats):
        super().__init__(brand, model)
        self.seats=seats


    def get_seat(self):    
        return self.seats
    
    def display(self):
        print(f"Car -> Brand: {self.brand}, Model: {self.model}, Seats: {self.seats}")


class Bike(Vehicle):
    def __init__(self, brand, model,engine_cc):
        super().__init__(brand, model)
        self.engine_cc=engine_cc


    def get_engine_cc(self):
        return self.engine_cc   
    
    def display(self):
        print(f"Bike -> Brand: {self.brand}, Model: {self.model}, Engine CC: {self.engine_cc}")


c = Car("Toyota", "Corolla", 5)
b = Bike("Honda", "CBR500R", 500)

c.display()   

b.display()