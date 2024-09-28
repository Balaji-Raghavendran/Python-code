class chocolateicecream():
    def __init__(self):
        print("chocolate ice cream ready")
    def icecream1(self):
        print("chocolate price 200")

class vanillaicecream():
    def __init__(self):
        super().__init__()
        print("vanilla ice cream is ready")
    def icecream2(self):
        print("vanilla price 180")

class butterscotch(vanillaicecream,chocolateicecream):
    def __init__(self):
        super().__init__()
        print("butterscotch is ready")
    def icecream3(self):
        print("butterscotch price 250")

customer=butterscotch()
customer.icecream3()


