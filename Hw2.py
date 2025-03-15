class Bike: 
    def __init__(self, brand, model, fuel, col): 
        self.brand = brand
        self.model = model
        self.fuel = fuel
        self.col = col

    def showBike(self): 
        print("Brand: ", self.brand, " Model: ", self.model, " Fuel: ", self.fuel, " Col: ", self.col)

class SportsBike(Bike): 
    def __init__(self, brand, model, fuel, col, topSpeed, abs):
        super().__init__(brand, model, fuel, col)
        self.topSpeed = topSpeed
        self.abs = abs

    def showBike(self): 
        #super()
        print("Brand: ", self.brand, " Model: ", self.model, " Fuel: ", self.fuel, " Col: ", self.col, " topSpeed: ", self.topSpeed, " abs: ", self.abs)

obj1= Bike("Tata", "Amg1", "Petrol", "Black")
obj2 = SportsBike("Tata", "Amg1", "Petrol", "Black", "560 kmph", "True")
obj1.showBike()
obj2.showBike()
    