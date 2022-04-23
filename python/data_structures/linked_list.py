class LinkedList:
    """
    Put docstring here
    """

    def __init__(self):
        # initialization here
        self.head = None

    # Create a new Node that has the correct value
    def insert(self, value):
        # method body here
        new_node = Node("apple")
        self.head = Node(value)


class Node:
    def __init__(self, value):
        self.value = value


class TargetError:
    pass
