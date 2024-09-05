class kodaikanal:
    name = ""
    hotelname = ""
    touristspot = ""

    def coffee(self):
        print("enjoying the coffee...")
    def tea(self):
        print("enjoying tea....")

john = kodaikanal()
austin = kodaikanal()
dwayne = kodaikanal()

john.name = "john"
austin.name = "austin"
dwayne.name = "dwayne"

john.hotelname = "kodaikanal 5 star hotel"
austin.hotelname = "frenzy hotel"
dwayne.hotelname = "premium palazo"

john.touristspot = "Silver cascade falls"
austin.touristspot = "Kodaikanal Lake"
dwayne.touristspot = "Guna cave"

print("name:"+john.name)
print("Hotel you want to stay:"+austin.hotelname)
print("Tourist spot you want to visit:"+dwayne.touristspot)

john.tea()