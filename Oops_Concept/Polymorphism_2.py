class Car:
    def __init__(self,brand,model):
        self.brand=brand
        self.model=model
    def move(self):
        print("car is moving")

class Boat:
    def __init__(self,brand,model):
        self.brand=brand
        self.model=model
    def move(self):
        print("Boat is Sailing")

class Plane:
    def __init__(self,brand,model):
        self.brand=brand
        self.model=model
    def move(self):
        print("Plane is flying")

car1 = Car("Lamborgini","Huracan LP 610 4 Coupe")
boat1 = Boat("The Bertram","Model 35")
plane1 =Plane("Airbus","Model A380")

car1.move()