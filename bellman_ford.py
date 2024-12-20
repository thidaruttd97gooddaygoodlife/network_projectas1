class BellmanFord:
    def __init__(self, graph):
        self.graph = graph
        self.adj_list = graph.get_adj_list()

    def detect_negative_cycle(self):
        nodes = list(self.adj_list.keys())
        distances = {node: float('inf') for node in nodes}
        distances[0] = 0  # Set the source node (usually node 0) to 0
        predecessors = {node: None for node in nodes}

        # Bellman-Ford algorithm to find the shortest paths
        for iteration in range(len(nodes) - 1):
            print(f"Iteration {iteration}:")
            for u in nodes:
                for v, weight in self.adj_list[u]:
                    print(f"Processing edge {u} -> {v} with weight {weight}")
                    if distances[u] + weight < distances[v]:
                        distances[v] = distances[u] + weight
                        predecessors[v] = u
                        print(f"Updated distance to node {v}: {distances[v]}")

        # Check for negative cycles
        for u in nodes:
            for v, weight in self.adj_list[u]:
                if distances[u] + weight < distances[v]:
                    print(f"Negative cycle detected via edge {u} -> {v} with weight {weight}")
                    return True, distances, predecessors

        return False, distances, predecessors
