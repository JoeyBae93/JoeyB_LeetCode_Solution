class Solution(object):
    def isValid(self, s):
        """
        :type s: str
        :rtype: bool
        
        Runtime: 7 ms (Beats 16.42%) | Memory: 12.47 mb (Beats 90.72%)
        """

        # create a stack
        stack = []

        # return False if s does not have at least two characters
        if len(s) < 2: return False
        
        # loop through s
        for ch in s:
            # multiple conditions
            # first, check if ch is opening bracket
            # if yes, stack it
            if ch == '(' or ch == '[' or ch == '{':
                stack.append(ch)
                
            # below statements check if ch is closing bracket
            # and if yes, return False either if stack is empty or if most recent stack is not the pair
            # otherwise, just pop most recent stack
            if ch == ')':
                if len(stack) != 0:
                    if stack[-1] != '(': return False
                    else: stack.pop()
                else:
                    return False
            if ch == ']':
                if len(stack) != 0:
                    if stack[-1] != '[': return False
                    else: stack.pop()
                else:
                    return False
            if ch =='}':
                if len(stack) != 0:
                    if stack[-1] != '{': return False
                    else: stack.pop()
                else:
                    return False
        
        # return True if stack is empty (meaning s is valid)
        # otherwise, False
        return len(stack) == 0  

        
print(Solution().isValid("()"))
print(Solution().isValid("()[]{}"))
print(Solution().isValid("(]"))
print(Solution().isValid("([)]"))
print(Solution().isValid("{[]}"))
print(Solution().isValid("(("))