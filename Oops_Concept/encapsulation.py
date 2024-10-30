class comapny:
    def __init__(self):
        self.__companyname="google"  # creating a private variable with a value
    
    def company_name(self):
        self.company = self.__companyname # assigning encapsulated value to a variable
        print(self.company) 

c1=comapny()
c1.company_name()
print(c1.__companyname) # this throws an error as it is private variable and can be used inside the class