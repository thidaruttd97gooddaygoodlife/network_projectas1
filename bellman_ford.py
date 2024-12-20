# bellman_ford.py
import time
import random  # Random module for simulating network delay
from collections import defaultdict
from graph import DistributedGraph

class DistributedBellmanFord:
    def __init__(self, graph, source):
        # Initialize the Bellman-Ford algorithm
        self.graph = graph
        self.source = source
        self.distances = defaultdict(lambda: float('inf'))  # Initializing distances to infinity
        self.predecessors = defaultdict(lambda: None)  # For storing predecessors of each node
        self.distances[source] = 0  # The source node has a distance of 0

    def run(self):
        iteration = 0
        while True:
            print(f"\n{'-'*40}")
            print(f"Iteration {iteration}")
            print(f"{'-'*40}")
            updated = False  # Flag to check if any update occurs

            # For each node in the graph, check its neighbors and update distances
            for node in self.graph.adj_list:
                for neighbor, weight in self.graph.get_neighbors(node):
                    new_distance = self.distances[node] + weight
                    if new_distance < self.distances[neighbor]:
                        print(f"  -> Updating distance of node {neighbor} "
                              f"from {self.distances[neighbor]} to {new_distance}")
                        self.distances[neighbor] = new_distance
                        self.predecessors[neighbor] = node
                        updated = True

            # Print distances after this iteration
            print(f"\nCurrent distances after iteration {iteration}:")
            print(f"{'Node':<6}{'Distance'}")
            print('-'*20)
            for node in sorted(self.distances.keys()):
                print(f"{node:<6}{self.distances[node]}")

            if not updated:
                print("\nNo updates in this iteration. Algorithm has converged.")
                break

            # Simulate communication delay between nodes (network latency)
            time.sleep(random.uniform(0.1, 0.3))  # Random delay between 0.1 to 0.3 seconds

            iteration += 1  # Increment iteration

        self.detect_negative_cycle()

    def detect_negative_cycle(self):
        # After completing the iterations, check for negative cycle
        for node in self.graph.adj_list:
            for neighbor, weight in self.graph.get_neighbors(node):
                if self.distances[node] + weight < self.distances[neighbor]:
                    print(f"\n{'*'*40}")
                    print(f"Negative cycle detected via edge {node} -> {neighbor} with weight {weight}")
                    print(f"{'*'*40}")
                    return True
        print("\nNo negative cycle detected.")
        return False
