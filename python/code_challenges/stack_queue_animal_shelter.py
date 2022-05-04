from data_structures.stack import Stack


class AnimalShelter:
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

    def enqueue(self, animal):
        self.stack_1.push(animal)

    def dequeue(self, pref):
        return_value = None
        # move items to stack 2
        while not self.stack_1.is_empty():
            self.stack_2.push(self.stack_1.pop())
        # move items back to stack 1 grabbing first instance of pref to return
        while not self.stack_2.is_empty():
            temp = self.stack_2.pop()
            # only grab the first match of pref
            if return_value is None:
                if pref == "dog" and str(temp) == "dog":
                    return_value = temp
                elif pref == "cat" and str(temp) == "cat":
                    return_value = temp
                else:
                    # not a match, push to stack 1
                    self.stack_1.push(temp)
            else:
                # push remaining items onto stack 1
                self.stack_1.push(temp)
        return return_value


class Dog:
    def __str__(self):
        return "dog"


class Cat:
    def __str__(self):
        return "cat"
