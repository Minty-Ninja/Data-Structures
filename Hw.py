class Appliance: 

    def use(self): 
        print("This appliance is in use")

class WashingMachine(Appliance): 
    def use(self): 
        print("THe Washing Machine is Washing clothes")

class Microwave(Appliance): 

    def use(self): 
        print("The Microwave is heating food")

obj1 = WashingMachine()
obj2 = Microwave()

obj1.use()
obj2.use()
