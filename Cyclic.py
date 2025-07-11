from collections import defaultdict

class graph:

    def __init__(self, vertex):
        self.graph = defaultdict(list)
        self.v = vertex

    def edges(self, node1, node2): 
        self.graph[node1].append(node2)
    
    def cycleUtil(self, vert, visited, recurstack): 

        visited[vert] = True
        recurstack[vert] = True
        for i in self.graph[vert]: 
            if visited[i] == False: 
                if self.cycleUtil(i, visited, recurstack) == True: 
                    return True
                
            elif recurstack[i] == True: 
                return True
        
        recurstack[vert] = False
        return False 
    

    def mainCycle(self):
        visited = [False] * (self.v+1) 
        recurstack = [False] * (self.v+1)
        for i in range(self.v): 
            if visited[i] == False: 
                if self.cycleUtil(i, visited, recurstack) == True: 
                    return True
        
        return False 
    


obj1 = graph(4) # Shud give yes = Cycle 
obj1.edges(1, 2)
obj1.edges(2, 1)
obj1.edges(2, 3)
obj1.edges(3, 1)
if obj1.mainCycle() == 1: 
    print("Graph has a cycle")
else: 
    print("Graph has no cycle")




