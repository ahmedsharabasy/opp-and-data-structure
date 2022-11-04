from collections import defaultdict

class graph:
    def __init__(self):
        self.graph=defaultdict(list)

    def addEdge(self,u,v):
        self.graph[u].append(v)

    def dfsutil(self,v,visited):
        visited.add(v)
        print(v,end='  ')
        for i in self.graph[v]:
            if i not in visited:
                self.dfsutil(i,visited)

    def dfs(self,s):
        visited=set()
        self.dfsutil(s,visited)            
        
g = graph()
g.addEdge(0, 1)
g.addEdge(0, 2)
g.addEdge(1, 2)
g.addEdge(2, 0)
g.addEdge(2, 3)
g.addEdge(3, 3)
 
print("Following is DFS from (starting from vertex 2)")
g.dfs(2)
