num = int(input("enter a number:"))
flag = False                         # creating a variable to check whether the divisor evenly dividing the number
if num == 1:                         # 1 does not have any two divisors therefore it is not a prime number.
    print("it is not a prime number")
elif num > 1:                      # to check the numbers which are higher than 1  
    for i in range(2,num):         # starting the values from 2 to end value - 1 to check it is prime number or not
        if num % i == 0:           # here if num divides i evenly and the reminder is 0 then it is not a prime number
            flag = True            # flag states true if the above condition satisfies
            break                  #loop gets break
if flag:
    print(num,"it is not a prime number")       #if the divisor is found then it is not a prime number
else:
    print(num,"it is a prime number")           #else divisor is not found then it is prime number.
        