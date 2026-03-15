class Solution(object):
    def groupAnagrams(self, strs):
        """
        :type strs: List[str]
        :rtype: List[List[str]]
        
        Runtime: 23 ms (Beats 53.76%) | Memory: 15.92 MB (Beats 94.18%)
        """
        
        # create a hash map for storing anagrams
        anagram_map = {}

        # loop through each word in the input list
        for word in strs:
            # turn a word into a key by sorting the characters (which creates a list of characters) and joining them back into a string
            # ex. "eat" "tea" "ate" will all become "aet"
            key = "".join(sorted(word))
            
            # either add a word into existing bucket or create a new bucket
            # setdefault() method is used to get the value of a key if it exists, otherwise it will set the key with a default value (in this case, an empty list) and return that default value
            anagram_map.setdefault(key, []).append(word)

        # return the values of the hash map (groups of anagrams) as list
        return list(anagram_map.values())
    
strs = ["eat","tea","tan","ate","nat","bat"]
print(Solution().groupAnagrams(strs))

strs = [""]
print(Solution().groupAnagrams(strs))

strs = ["a"]
print(Solution().groupAnagrams(strs))

strs = ["ddddddddddg","dgggggggggg"]
print(Solution().groupAnagrams(strs))