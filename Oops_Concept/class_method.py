class details():
    dept = 'BSC'

    def __init__(self):
        self.name="John"
        self.regno = "5"
        self.year="2024-27"

    def registerno(self,regnumber):
        self.regno = regnumber

    def changedregno(self):
        print(self.regno)

    @classmethod
    def changedeptname(cls):
        cls.dept="BCA"
        print(cls.dept,"successfully changed the dept")
        


student1 = details()
student1.registerno(10)
student1.changedregno()
print(student1.name)
print(student1.year)

details.changedeptname()

    
