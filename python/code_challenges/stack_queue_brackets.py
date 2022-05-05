from data_structures.stack import Stack
from data_structures.queue import Queue


def multi_bracket_validation(input):
    stack = Stack()
    opening_brackets = "([{"
    closing_brackets = ")]}"
    for char in input:
        if char in opening_brackets:
            stack.push(char)
        elif char in closing_brackets:
            if stack.is_empty():
                return False
            temp = stack.pop()
            # if temp doesn't match type of closing bracket
            match temp:
                case "{":
                    if not char == "}":
                        return False
                case "[":
                    if not char == "]":
                        return False
                case "(":
                    if not char == ")":
                        return False
    if not stack.is_empty():
        return False
    return True
