from nis import cat
from operator import truediv

from black import out
from data_structures.stack import Stack


class PseudoQueue:
    def __init__(self):
        self.stack_1 = Stack()
        self.stack_2 = Stack()

    def __str__(self):
        # add stack 1 to output
        output = "Stack 1: "
        current = self.stack_1.top
        if current == None:
            output += "NULL"
        else:
            while current is not None:
                output += f"{{ {str(current.value)} }} -> "
                current = current.next
            output += "NULL"

        # add stack 2 to output
        output += "\nStack 2: "
        current = self.stack_2.top
        if current == None:
            output += "NULL"
        else:
            while current is not None:
                output += f"{{ {str(current.value)} }} -> "
                current = current.next
            output += "NULL"
        return output

    def enqueue(self, value):
        self.stack_1.push(value)

    def dequeue(self):
        return_value = None
        # find return value and move others to stack 2
        cont = True
        while cont:
            try:
                value = self.stack_1.pop()
                return_value = value
                # next line of code will raise error and go to except at last stack item
                self.stack_1.peek()
                self.stack_2.push(value)
            except:
                cont = False
        # return non-dequeued items to stack 1
        cont = True
        while cont:
            try:
                value = self.stack_2.pop()
                self.stack_1.push(value)
            except:
                cont = False
        return return_value
