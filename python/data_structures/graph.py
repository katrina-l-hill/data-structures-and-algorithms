class Graph:
    """
    Put docstring here
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


class Vertex:
    def __init__(self, value):
        self.value = value
