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

    def pop(self):  # No arguments to pass in
        # method body here
        # Should raise exception when called on empty stack. Moved to the top of the method from the bottom due to error it was unreachable.
        if not self.top:
            raise InvalidOperationError("Method not allowed on empty collection")
            # Should return the node from the top of the stack
        old_top = self.top
        # Remove the node from the top of the stack
        self.top = self.top.next
        old_top.next = None
        # Returns teh value from the node from the top of the stack
        return old_top.value

    def peek(self):  # No arguments to pass in
        # method body here
        # Should raise an exception when called on empty stack
        if not self.top:
            raise InvalidOperationError("Method not allowed on empty collection")
            # Returns the value of the node located at the top of the stack
        return self.top.value

    def is_empty(self):  # No arguments to pass in
        # method body here
        # Returns a Boolean (True/False) indicating whether or not a stack is empty
        return self.size == 0
