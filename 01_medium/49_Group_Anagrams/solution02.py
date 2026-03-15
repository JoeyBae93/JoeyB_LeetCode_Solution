class Solution(object):
    def groupAnagrams(self, strs):
        """
        :type strs: List[str]
        :rtype: List[List[str]]
        
        Runtime: 31 ms (Beats 26.77%) | Memory: 18.16 MB (Beats 20.08%)
        """
        # create a hash map for storing anagrams
        anagram_map = {}
        
        # loop through each word in the input list
        for s in strs:
            # list of 26 alphabets initialized with count of 0
            count = [0] * 26
            
            # loop through each character in a word and count the frequency of each character
            for c in s:
                # ord('a') gives the ASCII value of 'a', which is 97.
                # ord(c) - ord('a') would give the index of the character in the count list.
                count[ord(c) - ord('a')] += 1
            
            # convert the count list into a tuple, which can be used as a key in the hash map
            key = tuple(count)

            # either add a word into existing bucket or create a new bucket
            if key not in anagram_map:
                anagram_map[key] = []
                
            # append the original word into the corresponding bucket in the hash map
            anagram_map[key].append(s)
            
        return list(anagram_map.values())
    
    
strs = ["eat","tea","tan","ate","nat","bat"]
print(Solution().groupAnagrams(strs))

strs = [""]
print(Solution().groupAnagrams(strs))

strs = ["a"]
print(Solution().groupAnagrams(strs))

strs = ["ddddddddddg","dgggggggggg"]
print(Solution().groupAnagrams(strs))