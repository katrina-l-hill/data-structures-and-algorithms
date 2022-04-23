class LinkedList:
    """
    Put docstring here
    """

    def __init__(self):
        # initialization here
        self.head = None

    # Create a new Node that has the correct value
    def insert(self, value):
        self.head = Node(value, self.head)

    # value is the target value we're looking for to see if it's included in this list or not
    def includes(self, value):
        current = self.head
        while current:
            if current.value == value:
                return True
                # If we find the value we're looking for, it will return True and the while loop will exit as well as the function

            current = current.next
            # If current gets to the end after current.next then the value will be None and the function will go down to return False
        return False


class Node:
    def __init__(self, value, next=None):
        self.value = value
        self.next = next


class TargetError:
    pass
