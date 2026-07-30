class Solution:
    def merge(self, nums1, m, nums2, n):
        # Start from the end of nums1 and nums2
        i = m - 1  # pointer for nums1's valid elements
        j = n - 1  # pointer for nums2
        k = m + n - 1  # pointer for placement in nums1

        # Merge until one of the arrays is exhausted
        while i >= 0 and j >= 0:
            if nums1[i] > nums2[j]:
                nums1[k] = nums1[i]
                i -= 1
            else:
                nums1[k] = nums2[j]
                j -= 1
            k -= 1

        # If nums2 still has elements left, copy them
        while j >= 0:
            nums1[k] = nums2[j]
            j -= 1
            k -= 1
