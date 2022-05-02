# Stacks and Queues

Use a linked list as the underlying data storage mechanism to implement both a stack and a queue.

## Challenge

The challenge is to be able to push multiple values onto a stack, pop values off the stack, empty a stack after multiple pops, peek at the next item on the stack, instantiate a new stack, raise exceptions when popping and peeking, enqueue multiple values into a queue, dequeue out a queue, empty a queue after multiple dequeus, instantiante an empty queue, and raise exceptions when dequeing or peeking.

## Approach & Efficiency

My approach will be to create Node, stack, and queue classes, and add the push, pop, peek, and is empty methods to accomplish the challenges. The Big O for both Time and Space complexity is O(1) because the time it takes to find an access and element is the same regardless of the number of Nodes, and there is no additional memory needed for the algorithm to execute relative to the input size.

## API

There are no APIs used in this assignment.
