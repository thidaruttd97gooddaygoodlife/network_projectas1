# graph.py
class DistributedGraph:
    def __init__(self, nodes):
        self.adj_list = {node: [] for node in nodes}

    def add_edge(self, u, v, weight):
        self.adj_list[u].append((v, weight))

    def get_neighbors(self, node):
        return self.adj_list[node]
