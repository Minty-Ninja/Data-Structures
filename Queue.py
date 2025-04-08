class Queue():

    def __init__(self, length):
        self.queue = []
        self.length = length

    def enqueue(self, element):
        if len(self.queue)<self.length:
            self.queue.append(element) 
        else: 
            print("Queue is full")

    def dequeue(self):
        if len(self.queue) == 0:
            print("Empty Queue")
        else:
            self.queue.pop(0)

    def front(self): 
        if len(self.queue) == 0:
            print("Empty Queue")
        else:
            print(self.queue[0])
        
    def rear(self): 
        if len(self.queue) == 0:
            print("Empty Queue")
        else:
            print(self.queue[-1])

    def sizee(self):
        print(len(self.queue))

    def display(self):
        print(self.queue)

x = int(input("What's the size?"))
obj1 = Queue(x)
obj1.display()
obj1.enqueue(15)
obj1.enqueue(1234)
obj1.enqueue(98765)
obj1.enqueue(1293)
obj1.display()
obj1.dequeue()
obj1.sizee()
obj1.display()
obj1.front()
obj1.display()
obj1.rear()
obj1.display()