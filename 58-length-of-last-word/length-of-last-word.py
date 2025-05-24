class Solution:
    def lengthOfLastWord(self, s: str) -> int:
        end = len(s) - 1

        while end >= 0 and s[end] == ' ':
            end -= 1
        
        if end < 0:
            return 0
        
        start = end
        while start >=0 and s[start] != ' ':
            start -= 1
        
        return end - start
        