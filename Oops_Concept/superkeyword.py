class a:
    def __init__(self):
        print("a")
        def cls(self):
            print("you are in class A")

class b():
        def __init__(self):
             super().__init__() #superkeyword is used (i.e) to call the parent class's constructor
             print("b")
             def cls2(self):
                  print("you are in class b")

class c(b,a):
        def __init__(self):
             super().__init__() 
             print("c")
             def cls3(self):
                  print("you are in class c")

ob1=c()
