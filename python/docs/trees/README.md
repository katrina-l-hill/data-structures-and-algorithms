# 401 Data Structures, Code Challenges

## Trees

## Challenge Summary

This challenge is to traverse a Binary Tree and Binary Search Tree. The Binary Tree will be a depth first traversal with methods pre-order, in-order, and post-order. The Binary Search Tree will be a sub-class of fo the Binary Tree class and have the Add and Contains methods.

## Approach & Efficiency

The approach for this challenge is to start wtih the Binary Tree class. Create the three methods to traverse the tree and raise errors where applicable. The Binary Search Tree will import the Binary Tree and Node classes and use the Add and Contains methods to traverse the tree adding a value and returning a Boolean if the value isn't in the tree.

## API

pre_order(): this method looks at the root node first and output its value.
in_order(): this method looks at the left side children of the tree first, then up to the root, then down to the left side children.
post_order(): this method look at the left side children of the tree first, then over to the right side children, then up to the root.
add(): this method adds a new node with the value that's been passed in.
contains(): this method takes in a value and returns True or False if the value if in the tree at least one.
