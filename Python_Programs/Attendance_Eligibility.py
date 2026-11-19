total_students = int(input("enter no.of students:"))
eligible = 0                                        #creating case for eligible students
not_eligible = 0                                    #creating case for non-eligible students
for i in range(0,total_students):
        attendance = int(input(f"enter attendance of student {i+1} : "))      #using F-string method concantenates the i values in input method
        if attendance >= 75:
                print("Student",i+1,"eligible")
                eligible += 1                    #iterates eligible values according to the attendance percentage
        else:
                print("Student",i+1,"not eligible")
                not_eligible += 1                   #iterates non-eligible values according to the attendance percentage 

print("Total no of eligible Students:",eligible)
print("Total no of non-eligible Students:",not_eligible)
        
        
    
