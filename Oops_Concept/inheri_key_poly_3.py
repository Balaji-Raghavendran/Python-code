class employee:
    def __init__(self,name,salary):
        self.name=name
        self.salary=salary

class manager(employee):
    def __init__(self,name,department,salary):
        self.department=department
        super().__init__(name,salary)
    def display(self):
        print("Employee's name:",self.name)
        print("Employee's department:",self.department)
        print("Employee's salary:",self.salary)

emp1 = manager("Paul leveque","Testing",45000)
emp1.display()
