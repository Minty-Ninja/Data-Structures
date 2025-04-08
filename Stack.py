class Stacker:

    def __init__(self, length):
        self.list =[]
        self.length = length

    def Push(self, element):
        if len(self.list)<self.length:
            self.list.append(element)
        else: 
            print("Stack is already full")

    def Pop(self):
        if len(self.list) == 0:
            print("Stack is Empty")
        else:
            self.list.pop(-1)
    
    def top(self):
        if len(self.list) == 0:
            print("Stack is empty")
        else:
            print(self.list[-1])
        
    def Size(self):
        print (len(self.list))
    
    def display(self):
        print(self.list)


x = int(input("What length is needed?"))
obj1 = Stacker(x)
obj1.display()
obj1.Push(15)
obj1.Push(134)
obj1.Push(789)
obj1.Size()
obj1.top()
obj1.display()
obj1.Pop()
obj1.display()
