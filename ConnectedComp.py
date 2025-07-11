class dfs: 

    def __init__(self, node):
        self.node = node 
        self.list= [[] for i in range(node)]

    def edges(self, node1, node2):
        self.list[node1].append(node2)
        self.list[node2].append(node1)

    def DFShelp(self, temp1, vertex, visited):
        visited[vertex] = True
        temp1.append(vertex)
        for i in self.list[vertex]:
            if visited[i] == False:
                temp1 = self.DFShelp(temp1, i, visited)
        return temp1
    
    def connected(self):
        visited = []
        connectedList = []
        for i in range(self.node):
            visited.append(False)

        for i in range(self.node): 
            if visited[i] == False:  
                temp1 = []
                connectedList.append(self.DFShelp(temp1, i, visited))
        return connectedList


obj1 = dfs(5)
obj1.edges(1, 2)
obj1.edges(2, 4)
obj1.edges(3, 4)
print(obj1)

connectedComp = obj1.connected()
print(connectedComp)

        

