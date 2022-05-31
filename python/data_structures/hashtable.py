from data_structures.linked_list import LinkedList


class Hashtable:
    """
    Put docstring here
    """

    def __init__(self, size=1024):
        self.size = size
        self.buckets = [None] * self.size

    def __str__(self):
        output = ""
        for i in range(len(self.buckets)):
            if self.buckets[i] != None:
                current = self.buckets[i].head
                while current != None:
                    pair = current.value
                    output += f"({pair[0]}: {pair[1]})\n"
                    current = current.next
        return output

    def hash(self, key):
        sum_of_chars = 0
        for char in key:
            sum_of_chars += ord(char)
        primed = sum_of_chars * 599
        index = primed % self.size
        return index

    def set(self, key, value):
        index = self.hash(key)
        bucket = self.buckets[index]
        if bucket is None:
            bucket = LinkedList()
            self.buckets[index] = bucket
        current = bucket.head
        replaced = False
        while current != None:
            pair = current.value
            if len(pair) > 0 and pair[0] == key:
                replaced = True
                current.value = (key, value)
            current = current.next
        if not replaced:
            bucket.insert((key, value))

    def get(self, key):
        index = self.hash(key)
        bucket = self.buckets[index]
        if not bucket == None:
            current = bucket.head
            while current:
                pair = current.value
                current_key = pair[0]
                if current_key == key:
                    return pair[1]
                current = current.next
        return None

    def contains(self, key):
        index = self.hash(key)
        bucket = self.buckets[index]
        if not bucket == None:
            current = bucket.head
            while current:
                pair = current.value
                current_key = pair[0]
                if current_key == key:
                    return True
                current = current.next
        return False

    def keys(self):
        keyset = set()
        for bucket in self.buckets:
            if bucket != None:
                current = bucket.head
                while current != None:
                    pair = current.value
                    keyset.add(pair[0])
                    current = current.next
        return keyset


# test code with print
hashtable = Hashtable(1024)
hashtable.set("ahmad", 30)
hashtable.set("silent", True)
hashtable.set("listen", "to me")
print(hashtable.keys())
