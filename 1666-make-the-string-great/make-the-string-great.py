class Solution:
    def makeGood(self, s: str) -> str:
        stack = []

        for c in s:
            # print(stack[-1].lower(), c.lower(), ord(stack[-1]), ord(c))
            if stack:
                if stack[-1].lower() == c.lower() and ord(stack[-1]) != ord(c):
                    stack.pop()
                else:
                    stack.append(c)
            else:
                stack.append(c)

        
        return ''.join(stack)