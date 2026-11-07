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
