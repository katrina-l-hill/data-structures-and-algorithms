import pytest
from data_structures.binary_tree import BinaryTree, Node


# @pytest.mark.skip("TODO")
def test_node_exists():
    assert Node


# @pytest.mark.skip("TODO")
def test_create_node():
    node = Node("apple")
    assert node
    assert node.left is None
    assert node.right is None


# @pytest.mark.skip("TODO")
def test_tree_exists():
    assert BinaryTree


# @pytest.mark.skip("TODO")
def test_tree_root_exists():
    tree = BinaryTree()
    assert tree._root is None


# @pytest.mark.skip("TODO")
def test_pre_order(tree):
    actual = tree.pre_order()
    expected = ["a", "b", "d", "e", "c", "f", "g"]
    assert actual == expected


# @pytest.mark.skip("TODO")
def test_in_order(tree):
    actual = tree.in_order()
    expected = ["d", "b", "e", "a", "f", "c", "g"]  # left, root, right
    assert actual == expected


# @pytest.mark.skip("TODO")
def test_post_order(tree):
    actual = tree.post_order()
    expected = ["d", "e", "b", "f", "g", "c", "a"]
    assert actual == expected


@pytest.fixture
def tree():
    """
          a
      b      c
    d  e    f  g

    ["a", "b", "d", "e", "c", "f", "g"] - pre order
    ["d", "b", "e", "a", "f", "c", "g"] # in order - left, root, right

    """

    tree = BinaryTree()

    tree._root = Node("a")
    tree._root.left = Node("b")
    tree._root.right = Node("c")
    tree._root.left.left = Node("d")
    tree._root.left.right = Node("e")
    tree._root.right.left = Node("f")
    tree._root.right.right = Node("g")

    return tree
