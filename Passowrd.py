class lmao: 

    __password = "WWW"

    def __init__(self, name, email, usern): 
        self.name = name
        self.email = email
        self.usern = usern

    def getPassword(self): 
        return self.__password
    
    def setPassword(self): 
        oldp = input("Pls enter old password")

        if oldp == self.__password: 
            newP = input("Enter new Password")
            self.__password = newP

        else:
            print("Wrong Password. Enter again")

obj1 = lmao("Pascal", "WashingmAchine@gmail.com", "Paula")

print (obj1.name)
print (obj1.email)
print (obj1.usern)

obj1.setPassword()
