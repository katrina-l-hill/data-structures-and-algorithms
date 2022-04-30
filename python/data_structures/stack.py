from data_structures.linked_list import Node
from data_structures.invalid_operation_error import InvalidOperationError


class Stack:
    """
    Put docstring here
    """

    def __init__(self):
        # initialization here
        self.top = None

    def push(self, value):  # No arguments to pass in
        # method body here
        # Add a new node with that value to the top of the stack with an O(1) Time performance.
        self.top = Node(value, self.top)

    def pope(self):  # No arguments to pass in
        # method body here
        # Should return the node from the top of the stack
        old_top = self.top
        # Remove the node from the top of the stack
        self.top = self.top.next
        old_top.next = None
        return old_top.value
        # Should raise exception when called on empty stack
            if not self.top:
                raise InvalidOperationError("Method not allowed on empty collection")

    def peek(self):  # No arguments to pass in
        # method body here
        pass

    def is_empty(self):  # No arguments to pass in
        # method body here
        pass
