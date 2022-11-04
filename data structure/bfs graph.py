#a directed graph

from collections import defaultdict    #[('i', 4), ('p', 2), ('s', 4), ('m', 1)]

class graph:
    def __init__(self):
        self.graph=defaultdict(list)

    def addEdge(self,u,v):
        self.graph[u].append(v)

    def BFS(self,s):                # s   is the item which I will start from it
        visited=[False]*(max(self.graph)+1) 
        queue=[]
        queue.append(s)             # Mark the source node as visited and enqueue it
        visited[s]=True
        while queue:
            s=queue.pop(0)  #0بتشيل اول عنصر وده المطلوب اما فاضيه تشيل اخر عنصر      #list.pop(0) removes the first element. All remaining elements have to be shifted up one step
                             #list.pop() with no arguments removes the last element ,,There are no elements following so nothing needs to be shifted.
            print(s,end='  ')

            for i in self.graph[s]:
                if visited[i]==False:
                    queue.append(i)
                    visited[i]=True 


g=graph()
g.addEdge(0,1)
g.addEdge(0,2)
g.addEdge(1,2)
g.addEdge(2,0)
g.addEdge(2,3)
g.addEdge(3,3)

print ("Following is Breadth First Traversal"
    " (starting from vertex 2)") 
g.BFS(2)
