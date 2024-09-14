class calculator():
    def __init__(self,a,b):
        self.variable_a=a
        self.variable_b=b

    def calc(self):
        print("add:",self.variable_a+self.variable_b)
        print("sub:",self.variable_a-self.variable_b)
        print("mul:",self.variable_a*self.variable_b)
        print("div:",self.variable_a/self.variable_b)

integer = calculator(10,5)
integer.calc()



