a = int(input("enter 1st number:"))
b = int(input("enter 2nd number"))
while True:
    print('''Mini Calculator
             1.Add
             2.subtract
             3.multiply
             4.divide''')
    option = int(input("enter an option:"))
    if option == 1:
        add = a + b
        print(add)
    elif option == 2:
        sub = a - b
        print(sub)
    elif option == 3:
        mul = a * b
        print(mul)
    elif option == 4:
        div = a / b
        print(div)
        break
    else:
        print("invalid option")
