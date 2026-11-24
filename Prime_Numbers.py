text = input("enter a number:")
if text.isdigit():              #to check whether the provided string are in digits
    num = int(text)
    flag = False                #creating a variable name flag to know that divisor is not found and provided value as false
    if num == 1:                          
        print(num,"is not a prime number")
    elif num > 1:                        
        for i in range(2,num):   #starting the range from 2(as 1 and 0 are not prime numbers) and end num - 1       
            if num % i == 0:     # if num % i == 0 (i.e) either num value and divisor evenly divides or num value does not evenly divides 
                flag = True      #if divisor found flag value is true     
                break            #breaks the loop immediately
        if flag:      
            print(num,"is not a prime number")      
        else:
            print(num,"is a prime number") 
    else:
        print(num,"is not a prime number")       #if the provided value is zero the else case handles it
else:
    print("Invalid input")                     #either any inputs which does not belongs to prime number this else case handles them.
  

             
         
        