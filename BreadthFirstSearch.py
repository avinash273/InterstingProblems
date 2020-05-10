"""
implementing BFS traversal algorithms using adjacency list and queues
Time: O(V + E)
Space: (V)
"""

from collections import defaultdict


class Graph:
    def __init__(self):
        self.graph = defaultdict(list)

    def insertGraph(self, v1, v2):
        self.graph[v1].append(v2)

    def printGraph(self):
        print(self.graph)
        for node in self.graph:
            # print(node)
            for to in self.graph[node]:
                pass
                print(node, "->", to)

    def BFS(self, startNode):
        visited = set()
        queue = []
        queue.append(startNode)
        visited.add(startNode)

        while queue:
            u = queue.pop(0)
            print(u, end=" ")

            for v in self.graph[u]:
                if v not in visited:
                    queue.append(v)
                    visited.add(v)


newgraph = Graph()
newgraph.insertGraph(2, 1)
newgraph.insertGraph(2, 5)
newgraph.insertGraph(5, 6)
newgraph.insertGraph(5, 8)
newgraph.insertGraph(6, 9)
newgraph.insertGraph(9, 6)

newgraph.printGraph()

newgraph.BFS(2)
