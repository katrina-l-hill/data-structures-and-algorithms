import math

def BinarySearch (arr, search_term):
    begin = 0
    end = arr.length - 1
    while begin <= end:
        middle = math.floor(begin + end)
        if arr(middle) < search_term:
            begin = middle + 1
        elif arr(middle) > search_term:
            end = middle - 1
        else:
            return middle
            print('The index of the array\'s element that is equal to the value of the search key is {search_term}.')
    return -1
    print('The element is not in the array')


