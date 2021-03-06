class Graph:
    """
    Utilized instructor's demo code and tests for this code challenge.
    """

    def __init__(self):
        # initialization here
        self._adjacency_list = {}

    def add_node(self, value):
        vertex = Vertex(value)
        self._adjacency_list[vertex] = []
        return vertex
        # a vertex uses its memory address as hash
        # value is initially an empty list

    def size(self):
        return len(self._adjacency_list)
        # could also use key(method)

    def get_nodes(self):
        return self._adjacency_list.keys()

    def add_edge(self, start_vertex, end_vertex, weight=0):
        if (
            start_vertex not in self._adjacency_list
            or end_vertex not in self._adjacency_list
        ):
            raise KeyError
        edge = Edge(end_vertex, weight)
        # edge wants to know what it's being connected to --> end_vertex and a weight
        list_of_edges = self._adjacency_list[start_vertex]
        list_of_edges.append(edge)

    def get_neighbors(self, vertex):
        return self._adjacency_list[vertex]


class Vertex:
    def __init__(self, value):
        self.value = value


class Edge:
    def __init__(self, vertex, weight):
        self.vertex = vertex
        self.weight = weight
