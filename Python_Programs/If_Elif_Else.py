age = int(input("Enter your age:")) #receives input from the user

if age >= 18: #condition for if statement
    print("You are already eligible to vote")
elif age == 18: #condition for elif statement
    print("You have become eligible to vote")
else: #else statement when both the above statements does not match
    print("You are not eligible to vote")