# Pseudo code:

# ALGORITHM Mergesort(arr)
#     DECLARE n <-- arr.length

#     if n > 1
#       DECLARE mid <-- n/2
#       DECLARE left <-- arr[0...mid]
#       DECLARE right <-- arr[mid...n]
#       // sort the left side
#       Mergesort(left)
#       // sort the right side
#       Mergesort(right)
#       // merge the sorted left and right sides together
#       Merge(left, right, arr)

# ALGORITHM Merge(left, right, arr)
#     DECLARE i <-- 0
#     DECLARE j <-- 0
#     DECLARE k <-- 0

#     while i < left.length && j < right.length
#         if left[i] <= right[j]
#             arr[k] <-- left[i]
#             i <-- i + 1
#         else
#             arr[k] <-- right[j]
#             j <-- j + 1

#         k <-- k + 1

#     if i = left.length
#        set remaining entries in arr to remaining values in right
#     else
#        set remaining entries in arr to remaining values in left


def merge_sort(array, depth=1):
    n = len(array)

    if n > 1:
        mid = n // 2
        left_half = array[0:mid]
        right_half = array[mid:n]

        print(f"depth: {depth}\nleft_half: {left_half}\nright_half: {right_half}\n")

        # sort the left side
        merge_sort(left_half, depth + 1)

        # sort the left side
        merge_sort(right_half, depth + 1)

        # merge the sorted left and right sides together
        merge(left_half, right_half, array)

        return array


def merge(left_half, right_half, array):
    i = 0
    j = 0
    k = 0
    while i < len(left_half) and j < len(right_half):
        print(
            f"\ti: {i}\n\tj: {j}\n\tk: {k}\n\tleft_half: {left_half}\n\tright_half: {right_half}\n\tarray: {array}\n"
        )
        if left_half[i] <= right_half[j]:
            array[k] = left_half[i]
            i += 1
        else:
            array[k] = right_half[j]
            j += 1
        k += 1
    if i == len(left_half):
        # set remaining entries in array equal to remaining values in right
        while j < len(right_half):
            array[k] = right_half[j]
            j += 1
            k += 1
    else:
        # set remaining entries in array equal to remaining values in left
        while i < len(left_half):
            array[k] = left_half[i]
            i += 1
            k += 1

    return array


list = [8, 4, 23, 42, 16, 15]
print(merge_sort(list))
