class Solution:
    def isPalindrome(self, s: str) -> bool:
        s = ''.join(c.lower() if c.isalpha() or c.isnumeric() else '' for c in s)
        return s == s[::-1]