class Solution(object):
    def longestConsecutive(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        
        Runtime: 72 ms (beats 28.85%) | Memory: 21.30 mb (beats 93.09%)
        """
        # if nums is empty, return 0
        if not nums: return 0

        # sort the list
        nums.sort()

        # varibles which will be used to find the answer
        longest_count = 1
        count = 1

        # looping through the list to find the total count
        for i in range(len(nums) - 1):
            # if two numbers are same, skip to next number
            if nums[i] == nums[i + 1]:
                continue
            # if two numbers are consecutive, increase the count by 1
            if nums[i] + 1 == nums[i + 1]:
                count += 1
            # if not, exit out of the loop and return the total count
            else:
                longest_count = max(longest_count, count)
                count = 1

        # after successful for-loop run, make sure that
        # longest_count is still the longest
        return max(longest_count, count)