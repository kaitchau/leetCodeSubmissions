class Solution:
    def isValid(self, s: str) -> bool:
        pairs = {')':'(','}':'{',']':'['}
        stack = []
        for c in s:
            if c in pairs.keys():
                if stack and pairs[c] == stack[-1]:
                    stack.pop()
                else:
                    return False
            else:
                stack.append(c)
        return not stack

#

class Solution:
    def isValid(self, s: str) -> bool:
        pairs = {')':'(','}':'{',']':'['}
        stack = []
        for c in s:
            if c in pairs.keys():
                if stack and pairs[c] == stack[-1]:
                    stack.pop()
                else:
                    return False
            else:
                stack.append(c)
        return not stack
