# graph.py

import random

class DistributedGraph:
    def __init__(self, num_nodes):
        # Initialize the graph with the specified number of nodes
        self.num_nodes = num_nodes
        self.adj_list = {node: [] for node in range(num_nodes)}  # Adjacency list for each node

    def add_edge(self, source, dest, weight):
        # Add an edge to the graph
        self.adj_list[source].append((dest, weight))

    def get_neighbors(self, node):
        # Return the neighbors (and their weights) of a given node
        return self.adj_list[node]

    def print_graph(self):
        # Helper function to print the graph
        for node in self.adj_list:
            print(f"Node {node}:", self.adj_list[node])
