class Solution:
    def lengthOfLastWord(self, s: str) -> int:
        l, r = len(s)-1, len(s)-1

        while r>=0 and l>=0 and s[r] == ' ':
            r -= 1
            l -= 1
        
        while l >=0 and s[l] != ' ':
            l -= 1
        
        return len(s[l+1:r+1])
        