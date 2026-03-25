class Solution(object):
    def removeDuplicates(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        
        Runtime: 3ms (Beats 59.31%) | Memory: 13.19mb (Beats 96.69%)
        """
        # get the length of the array first
        # if length is 1, return 1
        length = len(nums)
        if length == 1: return 1
        
        # declare the first pointer
        ptr1 = 0

        # loop through the arrays with second pointer
        # if value at pointer 2 is not duplicate, move pointer 2 to right by 1
        # if value is duplicate, first move the pointer 1 to right by 1 and
        # change that value at pointer 1 to value at pointer 2
        while ptr2 < length:
            if nums[ptr1] == nums[ptr2]:
                ptr2 += 1
            else:
                ptr1 += 1
                nums[ptr1] = nums[ptr2]

        # return this value that will match with exact number of unique values
        return ptr1 + 1