from collections import deque

class Graph:

    def __init__(self):
        self.graph = {}

    def add_vertex(self, vertex):
        if vertex not in self.graph:
            self.graph[vertex] = []

    def add_edge(self, vertex1, vertex2):
        if vertex1 in self.graph and vertex2 in self.graph:
            self.graph[vertex1].append(vertex2)
            self.graph[vertex2].append(vertex1)
    
    def display(self):
        if self.graph:
            for vertex in self.graph:
                print(f"{vertex}: {self.graph[vertex]}")


    def bfs(self, start):
        visited = set() # To store non duplicate visited values
        queue = deque([start]) # Creating a Queue for keeping track
        result = []

        while queue:
            current_vertex = queue.popleft() # Pop the left value from the queue

            # We dont need to add the vertex that are already visited, so the condition must be there
            if current_vertex not in visited:
                visited.add(current_vertex)
                result.append(current_vertex)
                queue.extend(self.graph[current_vertex])

        return result
    




graph = Graph()

graph.add_vertex(0)
graph.add_vertex(2)
graph.add_vertex(1)
graph.add_vertex(3)
graph.add_vertex(4)
graph.add_vertex(5)
graph.add_vertex(6)


graph.add_edge(0, 2)
graph.add_edge(0, 1)
graph.add_edge(2, 3)
graph.add_edge(1, 4)
graph.add_edge(3, 4)
graph.add_edge(3, 6)
graph.add_edge(5, 4)
graph.add_edge(5, 6)


graph.display()

print(graph.bfs(0))