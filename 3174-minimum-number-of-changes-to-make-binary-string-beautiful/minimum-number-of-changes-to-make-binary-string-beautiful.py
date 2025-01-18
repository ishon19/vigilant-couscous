class Solution:
    def minChanges(self, s: str) -> int:
        res = 0
        consecutive = 1
        prev = s[0]
        
        for char in s[1:]:
            if char == prev:
                consecutive += 1
                continue
            
            if consecutive % 2 == 0:
                consecutive = 1
            else:
                consecutive = 0
                res += 1
            
            prev = char

        return res