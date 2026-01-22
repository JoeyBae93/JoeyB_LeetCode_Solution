class Solution(object):
    def longestConsecutive(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        
        Runtime: 71 ms (beats 30.01%) | Memory: 21.27 mb (beats 93.09%)
        """
        # sort the list
        nums.sort()

        # get the list length
        list_length = len(nums)

        # retunr 0 if list is empty
        if list_length == 0: return 0

        # count variable which will be incremented for each consecutive number
        # and return after counting is done
        count = 1

        # variable that will be used as answer
        longest_count = count

        # looping through the list to find the total count
        for i in range(list_length - 1):
            # if two numbers are same, skip to next number
            if nums[i] == nums[i + 1]:
                continue
            # if two numbers are consecutive, increase the count by 1
            if nums[i] + 1 == nums[i + 1]:
                count += 1
            # if not, exit out of the loop and return the total count
            else:
                if longest_count < count:
                    longest_count = count
                count = 1

        # after successful for-loop run, make sure that
        # longest_count is still the longest
        if longest_count < count:
            longest_count = count

        return longest_count
    