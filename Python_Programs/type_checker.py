value_1 = input("enter value 1:")  # providing a value which takes as a string
print(value_1.isdigit()) # prints the boolean value isdigit()
if value_1.isdigit():
    value_1 = int(value_1) #converting into string value


value_2 = input("enter value 2:")
print(value_2.isdigit())
if value_2.isdigit():
    value_2 = int(value_2)



value_3 = input("enter value 3:")
print(value_3.isdigit())
if value_3.isdigit():
    value_3 = int(value_3)

if isinstance(value_1,int) and isinstance(value_2,int) and isinstance(value_3,int): # checks whether the isinstance(object, type) matches
    total = value_1 + value_2 + value_3 #adding up the values
    print(total)
else:
    print("Cannot able to add") #if the object and type doesn't match falls to the else statement
