class frnd1():
    def playstation(self):
        print("frnd1's playstation")

class frnd2(frnd1):
    def books(self):
        print("frnd2's books")

class frnd_3(frnd2):  
    def laptop(self):
        print("frnd3's laptop")

lionel=frnd_3()
suarez=frnd2()
neymar=frnd1

suarez.playstation()
lionel.books()



