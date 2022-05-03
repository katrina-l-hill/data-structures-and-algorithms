from data_structures.stack import Stack
from data_structures.linked_list import Node


class PseudoQueue:
    def __init__(self, stack_1, stack_2):
        self.stack_1 = stack_1
        self.stack_2 = stack_2

    def enqueue(self, value):
        self.stack_1.push(value)

    def dequeue(self):
        # temp = self.stack_1.pop()
        # self.stack_2.push(temp)
        return_value = None
        value = self.stack_1.pop()
        while value is not None:
            if self.stack_1.peek() != None:
                self.stack_2(value)
            else:
                return_value = self.stack_1.peek()
            value = self.stack_1.pop()
        value = self.stack_2.pop()
        while value is not None:
            self.stack_1.push(value)
            value = self.stack_2.pop()
        return return_value
