class Solution:
    def longestValidParentheses(self, s: str) -> int:
        # Stack to hold indices
        stack = [-1]  # Initialize with -1 to handle base case
        max_len = 0

        for i, char in enumerate(s):
            if char == '(':
                stack.append(i)
            else:
                stack.pop()  # Match with last unmatched '('
                if not stack:
                    stack.append(i)  # Reset base index
                else:
                    max_len = max(max_len, i - stack[-1])

        return max_len
