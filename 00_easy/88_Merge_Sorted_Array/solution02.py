class Solution(object):
    def merge(self, nums1, m, nums2, n):
        """
        :type nums1: List[int]
        :type m: int
        :type nums2: List[int]
        :type n: int
        :rtype: None Do not return anything, modify nums1 in-place instead.
        
        Runtime: 0 ms (Beats 100%) | Memory: 12.4 mb (Beats 44.75%)
        """
        # replace the trailing zeros in nums1 with the items from nums2
        # how it works:
        # nums1 = [1, 2, 3, 0, 0, 0], m = 3
        # nums2 = [2, 5], n = 2
        # loop will target the trailing zeros in nums1, which first starts with m
        # loop will replace the zeroes with the items in nums2 for n amount of time
        # nums1 before sort will be like this: [1, 2, 3, 2, 5, 0]
        for i in range(n):
            nums1[m + i] = nums2[i]
        
        # sort the nums1
        nums1.sort()