# main.py
from graph import DistributedGraph
from bellman_ford import DistributedBellmanFord
import random

if __name__ == "__main__":
    # Create a graph with 30 nodes
    num_nodes = 30
    graph = DistributedGraph(num_nodes)

    # Add some random edges between nodes
    for _ in range(100):  # Adding 100 random edges with random weights
        source = random.randint(0, num_nodes-1)
        dest = random.randint(0, num_nodes-1)
        weight = random.randint(1, 10)  # Random weight between 1 and 10
        graph.add_edge(source, dest, weight)

    # Print the graph for reference
    print("Graph structure:")
    graph.print_graph()

    # Choose a source node (e.g., node 0)
    source_node = 0

    # Run the Distributed Bellman-Ford algorithm
    d_bf = DistributedBellmanFord(graph, source_node)
    d_bf.run()
