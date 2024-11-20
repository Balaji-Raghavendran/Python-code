class person:
    def __init__(self,name,age):
        self._name = name
        self._age = age

    def person_details(self):
       print("name:"+self._name+", age:"+str(self._age))

class student(person):
    def __init__(self,student_name,student_age,student_id):
        super().__init__(student_name, student_age)
        self._id = student_id

    def student_details(self):
        print("Student Id:"+self._id)
        self.person_details()

student1 = student("Williamson",19,"A125")
student1.student_details()