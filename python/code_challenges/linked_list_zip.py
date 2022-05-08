from data_structures.linked_list import LinkedList, Node

# method to assign a head
def zip_lists(a, b):

    # create new linked list instance from imported class LinkedList
    output = LinkedList()

    # create variable to track position in list a and b
    position_a = a.head
    position_b = b.head

    # while loop that runs while either current position is not null
    while position_a != None or position_b != None:

        # in while loop, alternate appending nodes to new list
        if position_a != None:
            output.append(position_a.value)
            position_a = position_a.next
        if position_b != None:
            output.append(position_b.value)
            position_b = position_b.next

    # return the new list
    return output
