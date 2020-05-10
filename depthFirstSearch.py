"""
DFS implementation using Stack and Adjacency List on directed graphs
Time: O(V + E)
Space: (V)
"""

from collections import defaultdict


class Graph:
    def __init__(self):
        self.graph = defaultdict(list)

    def insertGraph(self, v1, v2):
        self.graph[v1].append(v2)
        """
        for undirected graph
        self.graph[v2].append(v1)
        """

    def printGraph(self):
        print(self.graph)
        for node in self.graph:
            # print(node)
            for to in self.graph[node]:
                pass
                print(node, "->", to)

    def DFS(self, startNode):
        visited = set()
        stack = []
        stack.append(startNode)

        while (len(stack)):
            cur = stack[-1]
            stack.pop()

            if (cur not in visited):
                print(cur, end=" ")
                visited.add(cur)

            for vertex in self.graph[cur]:
                if (vertex not in visited):
                    stack.append(vertex)


newgraph = Graph()
newgraph.insertGraph(2, 1)
newgraph.insertGraph(2, 5)
newgraph.insertGraph(5, 6)
newgraph.insertGraph(5, 8)
newgraph.insertGraph(6, 9)
newgraph.insertGraph(9, 6)

newgraph.printGraph()

newgraph.DFS(2)
