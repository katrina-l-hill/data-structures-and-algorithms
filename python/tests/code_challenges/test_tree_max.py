import pytest
from data_structures.binary_tree import BinaryTree, Node


# @pytest.mark.skip("TODO")
def test_max_val():
    tree = BinaryTree()
    tree._root = Node(10)
    tree._root.left = Node(30)
    tree._root.right = Node(-7)

    actual = tree.find_maximum_value()
    expected = 30

    assert actual == expected
