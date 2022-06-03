class Graph:
    """
    Put docstring here
    """

    def __init__(self):
        # initialization here
        self._adjacency_list = {}

    def add_node(self, value):
        return Vertex(value)

    def size(self):
        return len(self._adjacency_list)
        # could also use key(method)


class Vertex:
    def __init__(self, value):
        self.value = value
