def merge(self, nums1, m, nums2, n):
    nums3 = []
    i = 0
    j = 0
    k = 0

    while i < m and j < 2:
        if nums1[i] < nums2[j]:
            nums3[k] = nums1[i]
            k += 1
            i += 1
        else:
            nums3[k] = nums2[j]
            k += 1
            j += 1
            return nums3
