class Solution(object):
    def removeDuplicates(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        
        Runtime: 0ms (Beats 100.00%) | Memory: 13.94mb (Beats 33.34%)
        """
        # declare the first pointer
        ptr1 = 0

        # loop through the arrays with second pointer
        # if value at pointer 2 is equal to value at pointer 1
        # move the pointer 1 to right by 1 and make the value at that position equal to
        # the value at pointer 2
        for ptr2 in range(len(nums)):
            if nums[ptr2] != nums[ptr1]:
                ptr1 += 1
                nums[ptr1] = nums[ptr2]

        # return this value that will match with exact number of unique values
        return ptr1 + 1