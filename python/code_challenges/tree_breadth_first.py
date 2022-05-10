from data_structures.binary_tree import BinaryTree
from data_structures.queue import Queue


def breadth_first(tree):
    if tree is None:
        return []
    if tree.root is None:
        return []

    queue = Queue()
    list = []

    queue.enqueue(tree.root)
    while not queue.is_empty():
        current_node = queue.dequeue()
        list.append(current_node.value)
        if current_node.left is not None:
            queue.enqueue(current_node.left)
        if current_node.right is not None:
            queue.enqueue(current_node.right)
    return list
