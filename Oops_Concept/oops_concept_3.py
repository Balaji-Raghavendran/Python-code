class laptop():
    def __init__(self):
        self.laptopname=""
        self.ram=""
        self.processor=""
    def display(self):
        print("laptopmodel:",self.laptopname)
        print("ram:",self.ram)
        print("processor:",self.processor)


hp = laptop()
dell = laptop()

hp.laptopname="HP"
hp.ram="8gb"
hp.processor="i7"

dell.laptopname="DELL"
dell.ram="12gb"
dell.processor="i7"

hp.display()
dell.display()