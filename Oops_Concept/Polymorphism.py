class Animal:
    def sound(self):
        print("Animal makes sound")

class Dog(Animal):
    def sound(self):    # Method Overriding 
        print("Dog Barks")

class Bird(Animal):
    def sound(self):
        print("Bird Sings")


Parrot=Bird()
Parrot.sound()