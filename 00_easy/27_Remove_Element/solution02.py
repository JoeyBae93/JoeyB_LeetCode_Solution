class Solution(object):
    def removeElement(self, nums, val):
        """
        :type nums: List[int]
        :type val: int
        :rtype: int
        
        Runtime: 3ms (Beats 6.53%) | Memory: 12.25mb (Beats 95.92%)
        * Interesting thing to note is that only difference from solution02 and solution01 is that I removed code where it replaces remaining items in nums with '_'. Surprisngly, this cause runtime to decrease. It may be issue caused by LeetCode or my computer
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

        # return the value stored in the first pointer
        return pt1