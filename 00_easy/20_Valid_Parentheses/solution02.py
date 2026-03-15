class Solution(object):
    def isValid(self, s):
        """
        :type s: str
        :rtype: bool
        
        Runtime: 3 ms (Beats 75.41%) | Memory: 12.52 mb (Beats 61.74%)
        """
        # create a valid map
        # makes it easier to find opening pair of the closing bracket
        valid_map = {'': '', '(': ')', '{': '}', '[': ']'}
        
        # create a stack
        stack = []
        
        # loop through a string
        for ch in s:
            # if the character is one of the valid open paraentheses, stack it
            if ch in valid_map:
                stack.append(ch)
            # otherwise, return false if closing bracket
            # or if the most recent stacked character is not a pair
            elif not stack or valid_map[stack.pop()] != ch:
                return False

        # return True if stack is empty (meaning the s is valid)
        # otherwise False
        return not stack

        
print(Solution().isValid("()"))
print(Solution().isValid("()[]{}"))
print(Solution().isValid("(]"))
print(Solution().isValid("([)]"))
print(Solution().isValid("{[]}"))
print(Solution().isValid("(("))
print(Solution().isValid("]()"))