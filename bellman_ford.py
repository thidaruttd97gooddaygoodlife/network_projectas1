# bellman_ford.py
import time
from collections import defaultdict
from graph import DistributedGraph
import random 

class DistributedBellmanFord:
    def __init__(self, graph, source):
        self.graph = graph
        self.source = source
        self.distances = defaultdict(lambda: float('inf'))
        self.predecessors = defaultdict(lambda: None)
        self.distances[source] = 0

    def run(self, max_iterations=10):
        for iteration in range(max_iterations):
            print(f"Iteration {iteration}")
            updated = False

            for node in self.graph.adj_list:
                for neighbor, weight in self.graph.get_neighbors(node):
                    new_distance = self.distances[node] + weight
                    if new_distance < self.distances[neighbor]:
                        self.distances[neighbor] = new_distance
                        self.predecessors[neighbor] = node
                        updated = True

            if not updated:
                print("No updates in this iteration. Algorithm converged.")
                break

            # Simulate communication between neighbors
            time.sleep(random.uniform(0.1, 0.3))  # Simulate network delay

        self.detect_negative_cycle()

    def detect_negative_cycle(self):
        # Check for negative cycle by running one more iteration
        for node in self.graph.adj_list:
            for neighbor, weight in self.graph.get_neighbors(node):
                if self.distances[node] + weight < self.distances[neighbor]:
                    print(f"Negative cycle detected via edge {node} -> {neighbor} with weight {weight}")
                    return True
        print("No negative cycle detected.")
        return False
