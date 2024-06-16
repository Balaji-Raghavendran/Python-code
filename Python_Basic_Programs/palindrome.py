given_string = input("enter a text:")
reverse_string = ""

for i in given_string:
    reverse_string = i + reverse_string
if reverse_string == given_string:
    print("the given string is a palindrome")
else:
    print("it is not a palindrome")