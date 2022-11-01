class Graph:
    def __init__(self, graph_dict):
        if graph_dict is not None:
            self.graph_dict = []
        self.graph_dict = graph_dict

    def get_vertex(self):
        return list(self.graph_dict.keys())

    def get_edges(self):
        edges_list = []
        for vrtx in self.graph_dict.keys():
            for val in self.graph_dict[vrtx]:
                edge = vrtx+val
                if edge not in edges_list and val+vrtx not in edges_list:
                    edges_list.append(edge)

        return edges_list


graph_d = {
    "a": ['b', 'c'],
    'b': ['a', 'd'],
    'c': ['a', 'd'],
    'd': ['e'],
    'e': ['e'],
}

g = Graph(graph_d)
print(g.get_vertex())
print(g.get_edges())
