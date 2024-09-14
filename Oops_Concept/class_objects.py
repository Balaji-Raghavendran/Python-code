class student():
    def __init__(self):
        self.name = ""
        self.register_number = ""

    def details(self):
        print("name:",self.name)
        print("register no:",self.register_number)

s1 = student()
s2 = student()

s1.name = "Joe"
s1.register_number="80705"
s2.name = "Kendry"
s2.register_number="80706"

s1.details()
s2.details()

