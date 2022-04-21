from inspect import getblock
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
    return -1

def GetBinarySearchMessage (arr, search_term):
    result = BinarySearch(arr, search_term)
    if result == -1:
        print("-1. Element not found in the array.")
    else:
        print("Element found at index " + str(result))

GetBinarySearchMessage([4, 8, 15, 16, 23, 42], 15)
GetBinarySearchMessage([-131, -82, 0, 27, 42, 68, 179], 42)
GetBinarySearchMessage([11, 22, 33, 44, 55, 66, 77], 90)
GetBinarySearchMessage([1, 2, 3, 5, 6, 7], 4)
