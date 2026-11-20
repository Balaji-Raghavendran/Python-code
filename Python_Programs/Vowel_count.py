vowels = ['a','e','i','o','u','A','E','I','O','U']
count = 0
input_value = input("Enter a string:")            
for i in input_value:                  #input values iterates each string values in i
    if i in vowels:                    #checks if the values stored in i has vowels which is stored in vowels variable
        count += 1                     #the counts adds up when it is encountered a vowel
print(f"the word{input_value}has{count}vowels")