#Topological Sort
#Topological sorting for Directed Acyclic Graph (DAG) is a linear ordering of vertices such that for every directed edge uv from vertex u to vertex v, u comes before v in the ordering. Topological Sorting for a graph is not 
# possible if the graph is not a DAG.

# Given a Directed Acyclic Graph (DAG), the task is to find a linear order of its vertices such that for every directed edge u -> v, vertex u appears before v in the order. Topological Sorting is a technique used to arrange 
# vertices of a DAG in a sequence that respects all dependencies. It ensures that no vertex appears before any of its prerequisites.

#Using Kahn's Algorithm for Topological Sorting:(BFS based approach)
    # 1. Compute the in-degree (number of incoming edges) for each vertex and initialize a queue with all vertices having in-degree 0.
    # 2. While the queue is not empty, remove a vertex from the queue, add it to the topological order, and decrease the in-degree of its neighbors. If any neighbor's in-degree becomes 0, add it to the queue.
    # 3. Repeat until all vertices are processed. If the topological order contains all vertices, return it; otherwise, the graph has a cycle, and topological sorting is not possible.

from collections import deque, defaultdict

class Graph:
    def __init__(self):
        self.graph = defaultdict(list)

    def add_edge(self, u, v):
        self.graph[u].append(v)
        # Ensure destination vertices are included
        self.graph[v]

    def topological_sort(self):
        in_degree = {u: 0 for u in self.graph}

        for u in self.graph:
            for v in self.graph[u]:
                in_degree[v] += 1

        queue = deque(
            [u for u in self.graph if in_degree[u] == 0]
        )

        top_order = []

        while queue:
            u = queue.popleft()
            top_order.append(u)

            for v in self.graph[u]:
                in_degree[v] -= 1

                if in_degree[v] == 0:
                    queue.append(v)

        if len(top_order) != len(self.graph):
            raise ValueError(
                "Graph has at least one cycle; topological sorting not possible."
            )

        return top_order


g = Graph()

g.add_edge(5, 2)
g.add_edge(5, 0)
g.add_edge(4, 0)
g.add_edge(4, 1)
g.add_edge(2, 3)

try:
    print("Topological Sort of the given graph:", g.topological_sort())
except ValueError as e:
    print(e)






#Using recursive DFS-based approach for Topological Sorting
from collections import defaultdict

class Graph:
    def __init__(self, vertices):
        self.graph = defaultdict(list)
        self.V = vertices

    def addEdge(self, u, v):
        self.graph[u].append(v)

    def dfsSort(self, v, visited, stack):
        visited[v] = True
        for i in self.graph[v]:
            if not visited[i]:
                self.dfsSort(i, visited, stack)
        stack.insert(0, v)  # Add to front after exploring

    def topologicalSort(self):
        visited = [False] * self.V
        stack = []

        for i in range(self.V):
            if not visited[i]:
                self.dfsSort(i, visited, stack)

        print(stack)

g = Graph(6)
g.addEdge(5, 2)
g.addEdge(5, 0)
g.addEdge(4, 0)
g.addEdge(4, 1)
g.addEdge(2, 3)
g.addEdge(3, 1)

g.topologicalSort()

# Explanation:
# dfsSort() explores all dependencies of a node recursively before adding it to the stack.
# Nodes are inserted at the front of the stack only after all their children are processed.
# The final stack order [5, 4, 2, 3, 1, 0] ensures dependencies come before dependents.





#Using Iterative DFS-Based approach for Topological Sorting
#This method uses an iterative depth-first search (DFS) to perform topological sorting. It avoids recursion by using an explicit stack to manage the nodes to be processed. The algorithm ensures that each node is added to the 
# final stack only after all its dependencies have been processed, maintaining the correct order for topological sorting. 
# This method eliminates recursion and uses an explicit stack to simulate DFS traversal. It employs generators for efficient neighbor iteration and manually manages backtracking. This approach is useful for handling large graphs 
# without hitting recursion limits.

from collections import defaultdict
class Graph:
    def __init__(self, vertices):
        self.graph = defaultdict(list)
        self.V = vertices

    def addEdge(self, u, v):
        self.graph[u].append(v)

    def topologicalSort(self):
        visited = [False] * self.V
        stack = []

        for i in range(self.V):
            if not visited[i]:
                self.iterativeDFS(i, visited, stack)

        print(stack[::-1])  # Reverse the stack to get the correct order

    def iterativeDFS(self, start, visited, stack):
        temp_stack = [start]

        while temp_stack:
            node = temp_stack.pop()
            if not visited[node]:
                visited[node] = True
                stack.append(node)
                for neighbor in reversed(self.graph[node]):
                    if not visited[neighbor]:
                        temp_stack.append(neighbor)     
                        
g = Graph(6)
g.addEdge(5, 2)
g.addEdge(5, 0)
g.addEdge(4, 0)
g.addEdge(4, 1)
g.addEdge(2, 3)
g.addEdge(3, 1)
g.topologicalSort()

# Explanation:
# working_stack simulates recursion manually to avoid recursion depth issues.
# Each node’s neighbors are visited using iter(self.graph[v]) and pushed to the stack if unvisited.
# Nodes are inserted into the final stack after all neighbors are processed, maintaining dependency order.