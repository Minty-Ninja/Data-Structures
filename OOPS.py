#Creating a basic class w an object

class Fruits: 
    def __init__(self, col, shape, taste, size):
        self.col = col
        self.shape = shape
        self.taste = taste
        self.size = size


        #Creating the method

    def inputt(self):
        self.col = input("What is the colour?")
        self.shape = input("What is the shape?")
        self.taste = input("What is the taste?")
        self.size = input("What is the size?")


    def details(self):
        print("The colour is " +self.col)
        print("The shape is " +self.shape)
        print("The taste is " +self.taste)
        print("The size is " +self.size)



#Object creatin:
obj1 = Fruits("green", "round", "sweet", "medium")
obj1.details()  #Calling the method
obj1.inputt()
obj1.details()


#Private variables (Battery level)
class remote: 
    def __init__(self): 
        self.__battery_level = 100
        
    
    def press(self): 
        print("Channel changed")

obj1 = remote()
obj1.press()
#print(obj1.__battery_level)

#Inheritancee
class Animal: 
    def __init__(self): 
        print("ANimal class")

    def sound(self): 
        print("Animals make sound")

class cat(Animal):
    def __init__(self):
        print("Cats are animals")

    def sound(self): 
        print("Cats make a distinct sound")

class dog(Animal):
    def __init__(self):
        print("Dawgs are animals")

    def sound(self): 
        print("Dogs make a distinct sound")

obj1 = cat()
obj2 = dog()

obj1.sound()     
obj2.sound()