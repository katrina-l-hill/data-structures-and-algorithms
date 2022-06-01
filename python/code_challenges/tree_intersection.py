from data_structures.binary_tree import BinaryTree


def tree_intersection(tree_1, tree_2):
    set_1 = set(tree_1.pre_order())
    set_2 = set(tree_2.pre_order())
    return set_1.intersection(set_2)


