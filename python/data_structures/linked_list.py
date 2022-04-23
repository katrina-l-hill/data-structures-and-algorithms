class LinkedList:
    """
    This is a class that has a single head to start the initialization
    """

    # This is the initialization.
    def __init__(self):

        self.head = None

    # Create a new Node that has the correct value
    def insert(self, value):
        self.head = Node(value, self.head)

    # This searches for the target value we're looking for to see if it's included in this list or not
    def includes(self, value):
        current = self.head
        while current:
            if current.value == value:
                return True
                # If we find the value we're looking for, it will return True and the while loop will exit as well as the function

            current = current.next
            # If current gets to the end after current.next then the value will be None and the function will go down to return False
        return False

    def __str__(self):
        output = ""
        current = self.head
        if current == None:
            return "NULL"
        else:
            while current is not None:
                output += f"[{str(current.value)}] -> "
                current = current.next
            output += "NULL"
            return output


class Node:
    # Constructor to create Node class that has properties for the value stored in the Node, and a pointer to the next Node
    def __init__(self, value, next=None):
        self.value = value
        self.next = next


class TargetError:
    pass
