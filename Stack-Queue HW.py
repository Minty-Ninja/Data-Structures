class stack():

    def __init__(self, length):
        self.list = []
        self.length = length 

    def push(self, element):
        if len(self.list) < self.length:
            self.list.append(element)
        else:
            print ("Stack is full")
    
    def pop(self):
        if len(self.list) == 0:
            print("Stack doesn't have element")
        else:
            x= self.list.pop(-1)
            print("Element popped ", x)

    def top(self): 
        if len(self.list) == 0:
            print("Stack doesn't have element")
        else:
            print(self.list[-1])

    def check(self): 
        print("Stack size is ", len(self.list))

    def display(self):
        print(self.list)



class Queue():

    def __init__(self, length):
        self.list = []
        self.length = length

    def enqueue(self, element):
        if len(self.list) > self.length:
            print ("No space in queue")
        else:
            self.list.append(element)

    def dequeue(self):
        if len(self.list) == 0:
            print ("Queue is empty")
        else:
            x = self.list.pop(0)
            print (x)

    def viewFront(self):
        if len(self.list) == 0:
            print("Queue is empty")
        else:
            print(self.list[0])

    def viewBack(self):
        if len(self.list) == 0:
            print("Queue is empty")
        else:
            print(self.list[-1])

    def check(self): 
        print("Stack size is ", len(self.list))

    def display(self):
        print(self.list)


print("Welcome to Data Structure Playground. Choose a Data Structure to work with!")
while True: 
    print ("1. Stack")
    print("2. Queue")
    print("3. Exit")
    inp = int(input("What is your choice?")) 
    size = int(input("What size would u like?"))

    if  inp == 3:
        break

    elif inp == 2: 
        obj1 = Queue(size) 
        while True: 
            print("---Queue Menu---")
            print("1. Enqueue")
            print("2. Dequeue")
            print("3. View FrontElement")
            print("4. View Rear Element")
            print("5. Check Size")
            print("6. Display")
            print("7. Exit to Main Menu")

            x = int(input("What number?"))
            if (x==7):
                break

            elif (x==6):
                obj1.display()

            elif (x==5):
                obj1.check()

            elif (x==4):
                obj1.viewBack()

            elif (x==3):
                obj1.viewFront()

            elif (x==2):
                obj1.dequeue()

            elif (x==1):
                y = int(input("Element?"))
                obj1.enqueue(y) 

            else: 
                print("Invalid number")

    elif inp == 1:
        obj2 = stack(size)
        while True:
            print("---Stack Menu---")
            print("1. Push element")
            print("2. Pop element")
            print("3. View Top Element")
            print("4. Check Size")
            print("5. Display")
            print("6. Exit to Main Menu")

            x = int(input("What number?"))
            if (x == 6):
                break
            elif(x == 5):
                obj2.display()
            elif x== 4:
                obj2.check()
            elif x==3:
                obj2.top()
            elif x==2:
                obj2.pop()
            elif x==1:
                y = int(input("What element?"))
                obj2.push(y)
            else:
                print("Invalid Number")

    else:
        print("Invalid Number")
    

    



    


        
