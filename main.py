# main.py
from graph import DistributedGraph
from bellman_ford import DistributedBellmanFord

# Example: Create a graph with negative cycle
nodes = [0, 1, 2, 3]
graph = DistributedGraph(nodes)
graph.add_edge(0, 1, 5)
graph.add_edge(1, 2, 10)
graph.add_edge(2, 3, 3)
graph.add_edge(3, 1, 2)  # Negative cycle

# Run Distributed Bellman-Ford
source = 0
distributed_bellman_ford = DistributedBellmanFord(graph, source)
distributed_bellman_ford.run()

# Output results
print("Final Distances:")
for node, distance in distributed_bellman_ford.distances.items():
    print(f"Node {node}: {distance}")
