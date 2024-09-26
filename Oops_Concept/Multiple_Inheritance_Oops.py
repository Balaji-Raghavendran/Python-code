class airport:
    def flight(self):
        print("flying on the plane")

class ipad:
    def movie(self):
        print("watching movie")

class passenger(airport,ipad):  # used Multiple Inheritance on this particular class function
    def onboard(self):
        print("watching movie while travelling on plane")

Cristiano=passenger()
Cristiano.flight()
Cristiano.movie()
Cristiano.onboard()

