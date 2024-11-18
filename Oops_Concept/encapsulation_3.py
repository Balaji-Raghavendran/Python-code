class base:
    def __init__(self):
        self._a=2

class Derived(base):
     def __init__(self):
        base.__init__(self)
        print("Calling protected member of base class: ", self._a)
        self._a = 3 
        print("Calling modified protected member outside class: ",self._a)


obj1 = Derived()

obj2 = base()


print("Accessing protected member of obj1: ", obj1._a)
print("Accessing protected member of obj2: ", obj2._a)
