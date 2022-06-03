# 401 Data Structures, Code Challenges

## Graphs
<!-- Short summary or background information -->

## Challenge Summary

This challenge the implementation of a graph. The graph should be represented as an adjacency list, and should include the following methods: add_node(), add_edge(, get_nodes(), get_neighbors(), and size().

## Approach & Efficiency

The approach for this challenge was to review tests to help identify effiecient ways to write the methods.

The Big O notation for this algorithm: Time = O(n) for the time required to check every vertex for an adjacent vertex, and Space = O(1) for adding a node and/or edge.

## API

add_node(): this method adds a vertex(node) to a graph.
add_edge(): this method adds a connection between two nodes and takes in the weight of the connection.
get_nodes(): this method adds returns all the nodes in teh graph as a collection.
get_neighbors(): this method returns a collection of edges taht are connected to a given node.
size(): this method returns the total number of nodes in the graph.
