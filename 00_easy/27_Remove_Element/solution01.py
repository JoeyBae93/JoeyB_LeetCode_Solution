class Solution(object):
    def removeElement(self, nums, val):
        """
        :type nums: List[int]
        :type val: int
        :rtype: int
        
        Runtime: 0ms (Beats 100%) | Memory: 12.38mb (Beats 76.24%)
        """
        # declare the first pointer
        pt1 = 0
        
        # loop through the array (nums) using second pointer
        for pt2 in range(len(nums)):
            # if number at second pointer is not equal to targeted value
            if nums[pt2] != val:
                # move it to where first pointer is located, and move first pointer to next index
                nums[pt1] = nums[pt2]
                pt1 += 1
        
        # from where first pointer is located at, replace remaining items in the array as "_"
        for i in range(pt1, len(nums)):
            nums[i] == '_'

        # return the value stored in the first pointer
        return pt1