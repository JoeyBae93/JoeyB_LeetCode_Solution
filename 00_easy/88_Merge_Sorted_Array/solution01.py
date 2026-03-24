class Solution(object):
    def merge(self, nums1, m, nums2, n):
        """
        :type nums1: List[int]
        :type m: int
        :type nums2: List[int]
        :type n: int
        :rtype: None Do not return anything, modify nums1 in-place instead.
        
        Runtime: 0 ms (Beats 100%) | Memory: 12.31 mb (Beats 78.57%)
        """
        # remove the trailing zeros from nums1 for n times
        for i in range(n):
            if nums1[-1] == 0:
                nums1.pop()
            else:
                # break if there are no more trailing zeros
                break

        # append the items from nums2 to nums1 (merging)
        for item in nums2:
            nums1.append(item)

        # sort the nums1
        nums1.sort()