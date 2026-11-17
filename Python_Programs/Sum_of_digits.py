Val = input("enter a digit:") # entering a value 
total = 0 #to store the sum value
for i in Val: #iterating each values 
    if i.isdigit(): #to check whether the provided value a digit or not, skips if it's not a digit.
        total += int(i) #using int converting the string values into integer and sums up the digit
print(total) #prints the total value.