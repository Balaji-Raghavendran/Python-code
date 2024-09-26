#Program in single inheritance oops concept in python

class frnd1:
    def book(self):
        print("tobey's book")

class frnd2:
    def mobile(self):
        print("Andrew's mobile")

class frnd3(frnd1):
    def laptop(self):
        print("Tom's laptop")

Tom=frnd3()
Tom.book()

