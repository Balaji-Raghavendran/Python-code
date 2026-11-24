a = 7
b = 9
temp = 0 #creating a temporary variable to hold the value
temp = a # first temp holds a value and both the variable has value as 7
a = b # here we assign b value to a and it gets overriden but the temp already has value 7
b = temp #now the temp value will overrite the b's value 9 to 7.
print(a) #this will print 9
print(b) #this will print 7

