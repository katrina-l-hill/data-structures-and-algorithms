from ctypes import sizeof


class Hashtable:
    """
    Put docstring here
    """

    def __init__(self, size=1024):
        # initialization here
        pass
        self.size = size
        self.buckets = None

    def set(self, key, value):
        # compute the hash
        index = self.hash(key)
        pass

        # hash the key

        # set the key and value pair in the table

        # handle collisions

        # if key already exists, replace its value from teh value argument argument given in this method

        # returns nothing

    def get(self, key):
        # 1 - compute the hash
        index = self.hash(key)

        # 2 - go to the first node in the list at the bucket

        # 3 - traverse the linked list at this node

        # 4 while loop for node

        # 5 if statement for if node is the key or None
        # return the key is the current value
        # else return None
        pass

        # return value associated with that key in the table

    def contains(self, key):
        # compute the hash
        index = self.hash(key)
        pass

        # returns a Boolean indicating if the key exists in the table already

    def keys(self):
        # compute the hash
        pass

        # returns a collection of keys

    def hash(self, key):
        # method body here
        pass

        # returns an index in the collection for that key
        return index
