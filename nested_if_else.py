salary = int(input("enter your salary amount:"))
age = int(input("enter your age:"))
if salary >= 20000 or age <= 25:
    loan = int(input("enter your loan amount:"))
    if loan > 50000:
        print("maximum loan amount is 50000")
    else:
        print("loan amount will be provided")
else:
    print("you are not eligible for loan")