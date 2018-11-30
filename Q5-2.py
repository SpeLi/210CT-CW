from collections import defaultdict 
  
# This class represents a graph using adjacency list representation 
class Graph: 
  
    # Constructor 
    def __init__(self): 
  
        # default dictionary to store graph 
        self.graph = defaultdict(list) 
  
    # function to add an edge to graph 
    def addEdge(self,u,v): 
        self.graph[u].append(v) 
  
    # A function used by Dfs 
    def DfsUtil(self,v,visited): 
  
    # Mark the current node as visited and print it 
        visited[v]= True
        print (v) 
  
    # Recur for all the vertices adjacent to this vertex 
        for i in self.graph[v]: 
            if visited[i] == False: 
                self.DfsUtil(i, visited) 
  
  
    # The function to do Dfs traversal.
    # It uses recursive DfsUtil() 
    def Dfs(self,v): 
  
        # Mark all the vertices as not visited 
        visited = [False]*(len(self.graph)) 
  
        # Call the recursive helper function to print Dfs traversal 
        self.DfsUtil(v,visited) 
  
  
# testing 
# Create a graph given in the above diagram 
g = Graph() 
g.addEdge(0, 1) 
g.addEdge(0, 2) 
g.addEdge(1, 2) 
g.addEdge(2, 0) 
g.addEdge(2, 3) 
g.addEdge(3, 3) 
  
print ("Following is DFS from (starting from vertex 2)")
g.Dfs(2) 
