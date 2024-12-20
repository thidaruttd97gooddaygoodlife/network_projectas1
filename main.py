from graph import Graph
from bellman_ford import BellmanFord

# Initialize the graph with 6 nodes (0 to 5)
nodes = [0, 1, 2, 3, 4, 5]
graph = Graph(nodes)

# Add edges to the graph
graph.add_edge(0, 1, 4)
graph.add_edge(0, 2, 2)
graph.add_edge(1, 2, 3)
graph.add_edge(1, 3, 2)
graph.add_edge(2, 3, 3)
graph.add_edge(2, 4, 1)
graph.add_edge(3, 5, 4)
graph.add_edge(4, 5, -10)

# Create BellmanFord instance and run the algorithm
bellman_ford = BellmanFord(graph)
negative_cycle, distances, predecessors = bellman_ford.detect_negative_cycle()

# Output results
if negative_cycle:
    print("Negative cycle detected.")
else:
    print("Final Distances:")
    for node, distance in distances.items():
        print(f"Node {node}: {distance}")
