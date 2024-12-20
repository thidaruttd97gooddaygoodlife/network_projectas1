class Graph:
    def __init__(self, nodes):
        self.adj_list = {node: [] for node in nodes}

    def add_edge(self, u, v, weight):
        """ Add an edge from node u to node v with a given weight. """
        self.adj_list[u].append((v, weight))

    def get_adj_list(self):
        return self.adj_list
