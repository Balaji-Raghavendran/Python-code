# Simple tuple code
name = ('Dwayne','Hunter','Hardy')
print("the person's names:",name)
print("third person's name:",name[2])

# Simple dictionary code
Personal_details = {"name":"Hardy","Age":24,"gender":"male"}
print("Deatils of the selected third person:",Personal_details)

Personal_details["Profession"] = "Data Analyst"

print(Personal_details)

# Combining Tuples and dictionary together
Overall_details = {"names" : name,"Personal details of selected person":Personal_details}
print(Overall_details)