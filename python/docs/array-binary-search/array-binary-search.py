def BinarySearch (array, 1, n, x):
    if n >= 1:
        middle = 1 + (n - 1) // 2

        if array[middle] == x:
            return middle
        elif array[middle] > x:
            return BinarySearch(array, 1, middle - 1, x)
        else:
            return BinarySearch(array, middle + 1, n, x)
    else:
        return -1
