import math

def BinarySearch (arr, search_term):
    begin = 0
    end = len(arr) - 1
    while begin <= end:
        middle = math.floor(begin + end) // 2
        if arr[middle] < search_term:
            begin = middle + 1
        elif arr[middle] > search_term:
            end = middle - 1
        else:
            return middle
            print('The index of the array\'s element that is equal to the value of the search key is {search_term}.')
    return -1
    print('The element is not in the array')

print(BinarySearch([4, 8, 15, 16, 23, 42], 15))
print(BinarySearch([-131, -82, 0, 27, 42, 68, 179], 42))
print(BinarySearch([11, 22, 33, 44, 55, 66, 77], 90))
print(BinarySearch([1, 2, 3, 5, 6, 7], 4))

