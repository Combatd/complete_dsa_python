


# class Graph:
#     def __init__(self, gdict=None):
#         if gdict is None:
#             gdict = {}
#         self.gdict = gdict
    
#     def addEdge(self, vertex, edge):
#         self.gdict[vertex].append(edge)
    
#     def bfs(self, vertex):
#         visited = [vertex]
#         queue = [vertex]
#         while queue:
#             deVertex = queue.pop(0)
#             print(deVertex)
#             for adjacentVertex in self.gdict[deVertex]:
#                 if adjacentVertex not in visited:
#                     visited.append(adjacentVertex)
#                     queue.append(adjacentVertex)
    
#     def dfs(self, vertex):
#         visited = [vertex]
#         stack = [vertex]
#         while stack:
#             popVertex = stack.pop()
#             print(popVertex)
#             for adjacentVertex in self.gdict[popVertex]:
#                 if adjacentVertex not in visited:
#                     visited.append(adjacentVertex)
#                     stack.append(adjacentVertex)

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

    def remove_edge(self, vertex1, vertex2):
        if vertex1 in self.adjacency_list.keys() and vertex2 in self.adjacency_list.keys():
            try:
                self.adjacency_list[vertex1].remove(vertex2)
                self.adjacency_list[vertex2].remove(vertex1)
                return True
            except ValueError:
                pass
        return False

    def remove_vertex(self, vertex):
        if vertex in self.adjacency_list.keys():
            for other_vertex in self.adjacency_list[vertex]:
                self.adjacency_list[other_vertex].remove(vertex)
            del self.adjacency_list[vertex]
            return True
        return False
    

custom_graph = Graph()
custom_graph.add_vertex("A")
custom_graph.add_vertex("B")
custom_graph.add_edge("A", "B")
custom_graph.print_graph()

my_graph = Graph()
my_graph.add_vertex("A")
my_graph.add_vertex("B")
my_graph.add_vertex("C")
my_graph.add_vertex("D")
my_graph.add_edge("A", "B")
my_graph.add_edge("A", "C")
my_graph.add_edge("A", "D")
my_graph.add_edge("B", "C")
my_graph.add_edge("C", "D")
my_graph.print_graph()
print(my_graph.remove_vertex('D'), " <- Delete")
print("Print after remove")
my_graph.print_graph()
