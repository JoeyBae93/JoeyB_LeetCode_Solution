class Solution(object):
    def firstUniqChar(self, s):
        """
        :type s: str
        :rtype: int
        
        Runtime: 75 ms (beats 94.32%) | Memory: 12.41 mb (beats 99.18%)
        """
        
        # create a hash map to store the frequency of each character
        char_freq = {}
        
        # loop through the string and either add new character or increase the frequency of existing character in the hash map
        for char in s:
            if char in char_freq:
                char_freq[char] += 1
            else:
                char_freq[char] = 1
                                
        # loop through the string again to find the first unique character and return its index
        for i, char in enumerate(s):
            # if the frequency (the value of the key) is 1, return the index of the character
            if char_freq[char] == 1:
                return i
            
        return -1
        

print(Solution().firstUniqChar("leetcode") == 0)
print(Solution().firstUniqChar("loveleetcode") == 2)