class person:
    def __init__(self,name):  #constructor
        self.name=name

class student(person):
    def __init__(self,name,grade):
        super().__init__(name)  # using super keyword to inherit name from class person 
        self.grade=grade

    def display(self):
        print("Name is:",self.name)
        print("Grade is:",self.grade)

s1=student("Phil Brooks","A")
s1.display()