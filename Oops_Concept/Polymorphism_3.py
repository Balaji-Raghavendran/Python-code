class Area:
    def shape(self):
        print("the Area is:")

class Square(Area):
    def __init__(self,area):
        self.area=area
    def shape(self):
        a = self.area**2
        print("the area of square is:",a)

class Rectangle(Area):
    def __init__(self,length,breadth):
        self.length=length
        self.breadth=breadth
    def shape(self):
        b = self.length*self.breadth
        print("the area of rectangle is:",b)

a1 = Square(5)
b1 = Rectangle(10,5)
a1.shape()
b1.shape()
        