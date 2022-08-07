


# class Graph:
#     def __init__(self, gdict = None):
#         if gdict is None:
#             gdict = {}
#         self.gdict = gdict

#     def addEdge(self, vertex, edge):
#         self.gdict[vertex].append(edge)


# customDict = { "a" : ["b","c"],
#             "b" : ["a", "d", "e"],
#             "c" : ["a", "e"],
#             "d" : ["b", "e", "f"],
#             "e" : ["d", "f"],
#             "f" : ["d", "e"]
#                }

# graph = Graph(customDict)
# graph.addEdge("e", "c")
# print(graph.gdict["e"])

class Graph:
    def __init__(self):
        self.adjacency_list = {}

    def add_vertex(self, vertex):
        if vertex not in self.adjacency_list.keys():
            self.adjacency_list[vertex] = []
            return True
        return False
    
    def print_graph(self):
        for vertex in self.adjacency_list:
            print(vertex, ":", self.adjacency_list[vertex])

    def add_edge(self, vertex1, vertex2):
        if vertex1 in self.adjacency_list.keys() and vertex2 in self.adjacency_list.keys():
            self.adjacency_list[vertex1].append(vertex2)
            self.adjacency_list[vertex2].append(vertex1)
            return True
        return False


custom_graph = Graph()
custom_graph.add_vertex("A")
custom_graph.add_vertex("B")
custom_graph.add_edge("A", "B")
custom_graph.print_graph()