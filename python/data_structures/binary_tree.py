class Node:
    def __init__(self, value):
        self.value = value
        self.right = None
        self.left = None

    def __str__(self):
        return self.value


class BinaryTree:
    """
    Define a method for each of the depth traversals
    """

    def __init__(self):
        self.root = None

    def pre_order(self):
        def pre_order_recursive(node, current_list):
            current_list.append(node.value)
            if node.left is not None:
                pre_order_recursive(node.left, current_list)
            if node.right is not None:
                pre_order_recursive(node.right, current_list)
            return current_list

        pre_order_list = []
        pre_order_recursive(self.root, pre_order_list)
        return pre_order_list

    def in_order(self):
        def in_order_recursive(node, current_list):
            if node.left is not None:
                in_order_recursive(node.left, current_list)
            current_list.append(node.value)
            if node.right is not None:
                in_order_recursive(node.right, current_list)
            return current_list

        in_order_list = []
        in_order_recursive(self.root, in_order_list)
        return in_order_list

    def post_order(self):
        def post_order_recursive(node, current_list):
            if node.left is not None:
                post_order_recursive(node.left, current_list)
            if node.right is not None:
                post_order_recursive(node.right, current_list)
            current_list.append(node.value)
            return current_list

        post_order_list = []
        post_order_recursive(self.root, post_order_list)
        return post_order_list

    def find_maximum_value(self):
        def traverse_for_max(root, max=0):
            if root is None:
                return max
            if max < root.value:
                max = root.value

            left_side_value = traverse_for_max(root.left, max)
            if max < left_side_value:
                max = left_side_value

            right_side_value = traverse_for_max(root.right, max)
            if max < right_side_value:
                max = right_side_value

            return max

        return traverse_for_max(self.root)
