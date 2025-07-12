class Solution:
    def removeStars(self, s: str) -> str:
        stack = []

        for c in s:
            if not stack or c != '*':
                stack.append(c)
            else:
                stack.pop()

        return ''.join(stack)