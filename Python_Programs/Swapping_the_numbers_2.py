a = int(input("enter a number:"))
total = 0                            #creating a variable to store the swapped number
while a>0:                           #repeats the loop when digits are left in a variable and stops when it reaches 0
    rem = a % 10                     #gives the remainder value
    quo = a // 10                    #gives the number which is removed last
    a = quo                          #now a becomes smaller number because when every number is removed using // no number is left
    total = total * 10 + rem         # here this is key ex: a = 25 total = 0 therefore 0 = 0*10 + 5 now total value becomes 5
                                     #then again in second loop 5 = 5*10 + 2 = 52 therefore 25 is swapped as 52
print(total)
