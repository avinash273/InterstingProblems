"""
implementing graph in adjacency list
"""
from collections import defaultdict


class Graph:
    def __init__(self):
        self.graph = defaultdict(list)

    def insertNode(self, v1, v2):
        self.graph[v1].append(v2)

    def printGraph(self):
        print(self.graph)
        for node in self.graph:
            for to in self.graph[node]:
                print(node, "->", to)

g = Graph()
g.insertNode(2,1)
g.insertNode(1,2)
g.insertNode(2,3)
g.insertNode(3,4)
g.insertNode(1,4)


g.printGraph()
