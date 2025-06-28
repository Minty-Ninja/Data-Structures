class graph:

    def __init__(self, nodes):
        self.nodes = nodes
        self.adj = [[] for i in range(nodes)]

    def edges(self, node1, node2):
        self.adj[node1-1].append(node2-1)
        self.adj[node2-1].append(node1-1)

    def DFShelp(self, source, visited, order):
        order.append(source)
        visited[source] == True
        for node in self.adj[source]:
            if not visited[node]:
                self.DFShelp(node, visited, order)
    

    def mainDFS(self, source):
        visited = [False] * self.nodes
        order = []
        self.DFShelp(source, visited, order)
        return order
    
    
#Taking input and creating graph
x = int(input("How many nodes?"))

#Object creation
obj1 = graph(x)

y = int(input("How many edges?"))
print("Enter each edge like: 1 2")
for i in range(y):
    x,y = map(int, input().split())
    obj1.edges(x, y)

res = obj1.mainDFS(0)
print("DFS Traversal Order(1- based): ", [i+1 for i in res])



