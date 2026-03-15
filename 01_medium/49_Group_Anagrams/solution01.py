import collections

class Solution(object):
    def groupAnagrams(self, strs):
        """
        :type strs: List[str]
        :rtype: List[List[str]]
        
        Runtime: 35 ms (Beats 17.82%) | Memory: 18.17 MB (Beats 20.08%)
        """
        # create a hash map for storing anagrams
        ans = collections.defaultdict(list)
        
        # loop through each word in the input list
        for s in strs:
            # list of 26 alphabets initialized with count of 0
            count = [0] * 26
            
            # loop through each character in a word and count the frequency of each character
            for c in s:
                count[ord(c) - ord('a')] += 1
            
            # convert the count list into a tuple, which can be used as a key in the hash map
            ans[tuple(count)].append(s)
        
        # return the values of the hash map (groups of anagrams) as list
        return ans.values()
    
strs = ["eat","tea","tan","ate","nat","bat"]
print(Solution().groupAnagrams(strs))

strs = [""]
print(Solution().groupAnagrams(strs))

strs = ["a"]
print(Solution().groupAnagrams(strs))

strs = ["ddddddddddg","dgggggggggg"]
print(Solution().groupAnagrams(strs))