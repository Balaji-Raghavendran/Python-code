class dad:
    def money(self):
        print("dad's money")

class land:
    def importantland(self):
        print("family's land")

class son1:
    pass

class son2(dad,land):
    pass

class son3:
    pass

randy = son2()
randy.money()
randy.importantland()