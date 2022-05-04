from data_structures.linked_list import Node
from data_structures.invalid_operation_error import InvalidOperationError


class Stack:
    """
    Create a Stack class that has a top property. It creates an empty Stack when instantiated.
    """

    def __init__(self):
        # initialization here
        self.top = None

    def __str__(self):
        output = ""
        current = self.top
        if current == None:
            return "NULL"
        else:
            while current is not None:
                output += f"{{ {str(current.value)} }} -> "
                current = current.next
            output += "NULL"
            return output

    def push(self, value):  # Passing in value as an argument
        # method body here
        # Add a new node with that value to the top of the stack with an O(1) Time performance.
        if self.top is None:
            # adding first item, set next to None
            new_node = Node(value, None)
            self.top = new_node
        else:
            new_node = Node(value, self.top)
            self.top = new_node

    def pop(self):  # No arguments to pass in
        # method body here
        # Should raise exception when called on empty stack. Moved to the top of the method from the bottom due to error it was unreachable.
        if self.top is None:
            raise InvalidOperationError("Method not allowed on empty collection")
        # Store value from current top that is being popped off
        return_value = self.top.value
        self.top = self.top.next
        return return_value

    def peek(self):  # No arguments to pass in
        # method body here
        # Should raise exception when called on empty stack. Moved to the top of the method from the bottom due to error it was unreachable.
        if self.top is None:
            raise InvalidOperationError("Method not allowed on empty collection")
        # Store value from current top that is being popped off
        return self.top.value

    def is_empty(self):  # No arguments to pass in
        # method body here
        # Returns a Boolean (True/False) indicating whether or not a stack is empty
        return self.top is None
