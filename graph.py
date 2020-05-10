"""
implementing directed graph in adjacency list
"""
from collections import defaultdict


class Graph:
    def __init__(self):
        self.graph = defaultdict(list)

    def insertNode(self, v1, v2):
        self.graph[v1].append(v2)
        #to make it undirected graph
        self.graph[v2].append(v1)

    def printGraph(self):
        print(self.graph)
        for node in self.graph:
            for to in self.graph[node]:
                print(node, "->", to)

g = Graph()
g.insertNode(1,2)
g.insertNode(2,3)
g.insertNode(3,4)


g.printGraph()
