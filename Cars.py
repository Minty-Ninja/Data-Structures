class car: 

    def __init__(self, brand, model, fuel, col):
        self.brand = brand
        self.model = model
        self.fuel = fuel
        self.col = col

    def getcol(self): 
        return self.col
    
    def setcol(self):

        x = input("Give new colour")
        self.col = x

    def output(self): 
        print("Brand: "+ self.brand + "Model: " + self.model + "Fuel: " + self.fuel + "Color: " + self.col)

class SUV(car): 

    def __init__(self, brand, model, fuel, col, seating): 

        car.__init__(self, brand, model, fuel, col)
        self.seating = seating
    
    def output(self): 
        print(" Brand: "+ self.brand + " Model: " + self.model + " Fuel: " + self.fuel + " Color: " + self.col + " Seating: " + self.seating)
        
obj1 = SUV("SUV", "Mazda CX5", "Diesel", "black", "7")

print(obj1.getcol())
obj1.setcol()

obj1.output()