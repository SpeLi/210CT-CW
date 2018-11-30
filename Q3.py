class Graph():
    def __init__(self, graphdict=None):
        # initializes a graph object If no dictionary or None is given,
        # an empty dictionary will be used
        if graphdict == None:
            graphdict = {}
        self.graphdict = graphdict

    def vertices(self):
        # returns the vertices of a graph 
        return list(self.graphdict.keys())

    def edges(self):
        # returns the edges of a graph 
        return self.GenerateEdges()

    def addvertex(self, vertex):
        # If the vertex "vertex" is not in self.__graph_dict,
        # a key "vertex" with an emptylist as a value is added to the dictionary. 
        # Otherwise nothing has to be done. 
        if vertex not in self.graphdict:
            self.graphdict[vertex] = []

    def addedge(self, edge):
        # assumes that edge is of type set, tuple or list; 
        # between two vertices can be multiple edges 
        edge = set(edge)
        (vertex1, vertex2) = tuple(edge)
        if vertex1 in self.graphdict:
            self.graphdict[vertex1].append(vertex2)
        else:
            self.graphdict[vertex1] = [vertex2]

    def GenerateEdges(self):
        # A static method generating the edges of the graph "graph".
        # Edges are represented as sets with one (a loop back to the vertex) or two vertices 
        edges = []
        for vertex in self.graphdict:
            for neighbour in self.graphdict[vertex]:
                if {neighbour, vertex} not in edges:
                    edges.append({vertex, neighbour})
        return edges

    def __str__(self):
        res = "vertices: "
        for k in self.graphdict:
            res += str(k) + " "
        res += "\nedges: "
        for edge in self.__generate_edges():
            res += str(edge) + " "
        return res

#testing
if __name__ == "__main__":

    g = { "a" : ["d"],
          "b" : ["c"],
          "c" : ["b", "c", "d", "e"],
          "d" : ["a", "c"],
          "e" : ["c"],
          "f" : []
        }
    graph = Graph(g)

    print("Vertices of graph:")
    print(graph.vertices())

    print("Edges of graph:")
    print(graph.edges())

    print("Add vertex:")
    graph.addvertex("v","w")

    print("Vertices of graph:")
    print(graph.vertices())
 
    print("Add an edge:")
    graph.addedge({"a","z"})
    
    print("Vertices of graph:")
    print(graph.vertices())

    print("Edges of graph:")
    print(graph.edges())

    print('Adding an edge {"v","w"} with new vertices:')
    graph.addedge({"v","w"})
    print("Vertices of graph:")
    print(graph.vertices())
    print("Edges of graph:")
    print(graph.edges())
