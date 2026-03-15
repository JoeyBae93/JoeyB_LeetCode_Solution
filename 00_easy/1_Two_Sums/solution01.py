class Solution(object):
    def twoSum(self, nums, target):
        """
        :type nums: List[int]
        :type target: int
        :rtype: List[int]
        
        Runtime: 50 ms (beats 99.97%) | Memory: 15.28 mb (beats 99.98%)
        """
        # create a hash map
        numMap = {}
        
        # loop through the list and check if complement exists in the hash map
        for i, num in enumerate(nums):
            # ex. if target = 9, num = 2, then complement = 7
            complement = target - num
            
            # check if 7 exists in the hash map
            if complement in numMap:
                # if it does, return the index of 7 and the current index
                return [numMap[complement], i]
            
            # if it doesn't, add the current number and its index to the hash map
            numMap[num] = i
            
        # return empty list if no solution is found
        return []