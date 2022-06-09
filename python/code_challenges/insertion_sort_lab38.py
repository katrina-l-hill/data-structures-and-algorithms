# LeetCode: 147. Insertion Sort List
# Given the head of a singly linked list, sort the list using insertion sort, and return the sorted list's head.

# Pseudocode:

# class was already created and initialized from LeetCode

# define a function that method that in a list head
# set a temp variable equal to the list's first element
# set the current node to head
# set the previous node to the variable that takes in the list's first element
# while loop for current node:
# set the next node equal to the current node's next
# while loop if the previous' next node and the value of the previous next's node are less than the value of the current node
# then set the previous node equal to previous' next node
# set current's next node equal to the previous node
# set the previous' next node equal to the current node
# set the previous node equal to the temp variable
# set current equal to the next node
# return the next value in the temp variable


class ListNode(object):
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next


def insertionSortList(self, head):
    temp = ListNode(0)
    current_node = head
    previous_node = temp

    while current_node:
        next_node = current_node.next
        while previous_node.next and previous_node.next.val < current_node.val:
            previous_node = previous_node.next

            current_node.next = previous_node.next
            previous_node.next = current_node
            previous_node = temp
            current_node = next_node

    return temp.next
