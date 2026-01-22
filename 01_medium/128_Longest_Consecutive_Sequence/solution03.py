class Solution(object):
    def longestConsecutive(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        
        Runtime: 50 ms (beats 75.67%) | Memory: 27.17 mb (beats 20.05%)
        """
        # if nums is empty, return 0
        if not nums: return 0

        # create set out of the list and a return variable
        s = set(nums)
        longest = 0

        for i in s:
            # gatekeeping condition if number before i exists
            if (i - 1) not in s:
                length = 1
            
                # continue increase the length until last consecutive
                while (i + length) in s:
                    length += 1
                
                # make sure longest is longest
                longest = max(longest,length)

        # return the answer
        return longest