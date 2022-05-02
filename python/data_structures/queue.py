from data_structures.linked_list import Node
from data_structures.invalid_operation_error import InvalidOperationError


class Queue:
    """
    Put docstring here
    """

    def __init__(self):
        # initialization here
        self.front = None
        self.rear = None

    def __str__(self):
        output = ""
        current = self.front
        if current == None:
            return "NULL"
        else:
            while current is not None:
                output += f"{{ {str(current.value)} }} -> "
                current = current.next
            output += "NULL"
            return output

    def enqueue(self, value):  # Passing in value as an argument
        # method body here
        # Add a new node with that value to the back of the queue with an O(1) Time performance
        if self.rear is None:
            # adding item to empty queue
            new_node = Node(value, None)
            self.rear = new_node
            self.front = new_node
        else:
            new_node = Node(value, None)
            self.rear.next = new_node
            self.rear = new_node

    def dequeue(self):  # No arguments to pass in
        # Should raise exception when called on empty stack. Moved to the top of the method from the bottom due to error it was unreachable.
        if self.front is None:
            raise InvalidOperationError("Method not allowed on empty collection")
        # Returns the value from the node from the front of the queue
        return_value = self.front.value
        self.front = self.front.next
        if self.front is None:
            self.rear = None
        # Removes the node from the front of the queue
        return return_value

    def peek(self):  # No arguments to pass in
        # Should raise exception when called on empty stack. Moved to the top of the method from the bottom due to error it was unreachable.
        if self.front is None:
            raise InvalidOperationError("Method not allowed on empty collection")
        # Returns value of the node located at the front of the queue.
        return self.front.value

    def is_empty(self):  # No arguments to pass in
        # Returns a Boolean (True/False) indicating whether or not a queue is empty
        return self.rear is None
