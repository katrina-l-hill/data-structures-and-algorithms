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
                output += f"{{ {str(current.value)} }} -> "
                current = current.next
            output += "NULL"
            return output

    def append(self, new_value):
        new_node = Node(new_value)
        if self.head is None:
            self.head = new_node
            return
        last_node = self.head
        while last_node.next:
            last_node = last_node.next
        last_node.next = new_node

    def insert_before(self, value, new_value):
        # Need to identify if list is empty or not
        if self.head is None:
            raise TargetError
        new_node = Node(new_value)
        prev_node = None
        current_node = self.head
        found = False
        while current_node is not None:
            if current_node.value == value:
                found = True
                new_node.next = current_node
                if prev_node is not None:
                    prev_node.next = new_node
                else:
                    self.head = new_node
                return
            prev_node = current_node
            current_node = current_node.next
        if found == False:
            # value wasn't found in list raise error
            raise TargetError

    def insert_after(self, value, new_value):
        # Need to identify if list is empty or not
        if self.head is None:
            raise TargetError
        new_node = Node(new_value)
        current_node = self.head
        found = False
        while current_node is not None:
            # traverse the linked list to find node with node.value == value
            if current_node.value == value:
                # if match is found: current_node.next -> new_node AND set new_node.next -> node after
                found = True
                new_node.next = current_node.next
                current_node.next = new_node
                return
            current_node = current_node.next
        if found == False:
            # value wasn't found in list raise error
            raise TargetError

    def kth_from_end(self, k):
        if k < 0:
            current_node = self.head
            list_length = 0
            while current_node is not None:
                current_node = current_node.next
                list_length += 1
                return
        current_node = self.head
        for i in range(0, current_node - k):
            current_node = current_node.next
        print()


class Node:
    # Constructor to create Node class that has properties for the value stored in the Node, and a pointer to the next Node
    def __init__(self, value, next=None):
        self.value = value
        self.next = next


class TargetError(BaseException):
    pass
