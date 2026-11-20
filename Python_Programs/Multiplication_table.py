num = int(input("enter a number:"))
for i in range(1,11):              
    mul = num * i                 #here the num value and the loop i value multiplies until the range value - 1 and stores in mul
    print(f"{num}x{i}={mul}")