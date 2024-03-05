class Solution:
    def minimumLength(self, s: str) -> int:
        if len(s) == 1:
            return 1

        l, r = 0, len(s) - 1

        while l < r:
            if s[l] != s[r]:
                return r - l + 1
            else:
                look = s[l]

                while l < len(s) and s[l] == look:
                    l += 1

                while r >= 0 and s[r] == look:
                    r -= 1
        
        return max(0, r - l + 1)
                
                
