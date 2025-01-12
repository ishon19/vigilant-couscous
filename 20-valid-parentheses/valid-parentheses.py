class Solution:
    def isValid(self, s: str) -> bool:
        stack = []
        charMap = {'(': ')', '{': '}', '[':']'}

        for c in s:
            if not stack:
                stack.append(c)
            else:
                if stack[-1] in charMap.keys() and c == charMap[stack[-1]]:
                    stack.pop()
                else:
                    stack.append(c)
        
        return len(stack) == 0