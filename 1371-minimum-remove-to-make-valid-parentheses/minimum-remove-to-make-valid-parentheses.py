class Solution:
    def minRemoveToMakeValid(self, s: str) -> str:
        stack = []

        for idx, char in enumerate(s):
            if char in ['(', ')']:
                if stack and stack[-1][-1] == '(' and char == ')':
                    stack.pop()
                else:
                    stack.append([idx, char])

        skipIdx = set([idx for idx, _ in stack])
        res = ''
        for idx, char in enumerate(s):
            if idx not in skipIdx:
                res += char
        return res