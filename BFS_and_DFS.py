class graph:

    def __init__(self, nodes):
        self.nodes = nodes 
        self.adj = [[] for i in range(nodes)] 
        
    def edges(self, node1, node2): 
        self.adj[node1-1].append(node2-1)
        self.adj[node2-1].append(node1-1)

    def bfs(self, source): #Breath for Search
        visited = [False] * self.nodes
        order = []
        queue = []

        queue.append(source)
        visited[source] = True
        while len(queue) > 0:
            var = queue.pop(0)
            order.append(var)
            for i in self.adj[var]:
                if visited[i] == False:
                    queue.append(i)
                    visited[i] == True

        return order
    

#Graph creation
obj1 = graph(5)
obj1.edges(1,2)
obj1.edges(2,4)
obj1.edges(1,3)
obj1.edges(3,4)
print(obj1.bfs(0))




----------------------------------------------------------------------------------------------------------------------------------------
class graph:

    def __init__(self, nodes):
        self.nodes = nodes 
        self.adj = [[] for i in range(nodes)] 
        
    def edges(self, node1, node2): 
        self.adj[node1-1].append(node2-1)
        self.adj[node2-1].append(node1-1)

    def bfs(self, source): #Breath for Search
        visited = [False] * self.nodes
        order = []
        queue = []

        queue.append(source)
        visited[source] = True
        while len(queue) > 0:
            var = queue.pop(0)
            order.append(var)
            for i in self.adj[var]:
                if visited[i] == False:
                    queue.append(i)
                    visited[i] = True

        return order
    

#Graph creation
obj1 = graph(5)
obj1.edges(1,2)
obj1.edges(2,4)
obj1.edges(1,3)
obj1.edges(3,4)
obj1.edges(4, 5)
print(obj1.bfs(0))














