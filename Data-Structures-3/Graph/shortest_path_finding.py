import heapq

class WeightedGraph:

    def __init__(self):
        self.graph = {}
        self.vertex_index = {}
        self.edge_index = {}

    def add_vertex(self, vertex):
        if vertex not in self.graph:
            index = len(self.vertex_index)
            self.vertex_index[vertex] = index
            self.graph[vertex] = {}

    def add_edge(self, vertex1, vertex2, weight):
        if vertex1 in self.graph and vertex2 in self.graph:
            edge = (vertex1, vertex2)
            index = len(self.edge_index)
            self.edge_index[edge] = index
            self.graph[vertex1][vertex2] = weight
            self.graph[vertex2][vertex1] = weight


    def display(self):
        for vertex in self.graph:
            print(f"{vertex}: {self.graph[vertex]}")


    def dijkstra(self, start, end):
        distances = {vertex: float('inf') for vertex in self.graph}
        distances[start] = 0 # Initialize the start to zero
        priority_queue = [(distances[start], start)] # Create a priority queue tracking the distances and nodes
        visited = set()
        while priority_queue:
            (current_distance, current_vertex) = heapq.heappop(priority_queue)
            if current_distance in visited:
                continue
            visited.add(current_vertex)
            for neighbor, weight in self.graph[current_vertex].items():
                distance = current_distance + weight
                if distance < distances[neighbor]:
                    distances[neighbor] = distance
                    heapq.heappush(priority_queue, (distance, neighbor))

        print(distances)
        return distances
    
weighted_graph = WeightedGraph()

weighted_graph.add_vertex(0)
weighted_graph.add_vertex(1)
weighted_graph.add_vertex(2)
weighted_graph.add_vertex(3)
weighted_graph.add_vertex(4)

weighted_graph.add_edge(0, 1, 4)
weighted_graph.add_edge(0, 2, 1)
weighted_graph.add_edge(1, 3, 1)
weighted_graph.add_edge(2, 3, 5)
weighted_graph.add_edge(3, 4, 3)

weighted_graph.display()

print(weighted_graph.dijkstra(0, 4))