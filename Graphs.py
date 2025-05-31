class graphs:

    def __init__(self):
        self.graph = {}

    #Adding new node
    def newNode(self, root):
        if root not in self.graph:
            self.graph[root] = []
    
    #Function for adding edge between 2 nodes
    def edge(self, node1, node2, directed = False):
        if node1 not in self.graph:
            self.newNode(node1)
        if node2 not in self.graph:
            self.newNode(node2)
        
        self.graph[node1].append(node2)

        #Undirected graph
        if not directed:
            self.graph[node2].append(node1)

    #Display items
    def display(self):
        for i in self.graph:
            print(f"{i}:{self.graph[i]}")

    def deleteEdge(self, node1, node2, directed = False):
        if node1 in self.graph and node2 in self.graph[node1]: 
            self.graph[node1].remove(node2)

            if not directed and node1 in self.graph[node2]:
                self.graph[node2].remove(node1)
        else:
            print("Edge doesn't exist")
    
    def deleteNode(self, node):
        if node in self.graph:
            for i in self.graph:
                if node in self.graph[i]:
                    self.graph[i].remove(node)
            del self.graph[node]
        else:
            print("Node doesn't exist")




#Creating objects
obj1 = graphs()
obj1.newNode("A")
obj1.newNode("Z")
obj1.newNode("B")
obj1.newNode("C")
obj1.newNode("D")
obj1.newNode("F")

#Adding edges between the nodes
obj1.edge("A", "Z")
obj1.edge("Z", "B")
obj1.edge("B", "C")
obj1.edge("C", "D")
obj1.edge("D", "F")
obj1.edge("F", "A")


obj1.display()

#Deleting edge from C-D
obj1.deleteEdge("C", "D")
obj1.display()

#Removing F
obj1.deleteNode("F")
obj1.display()