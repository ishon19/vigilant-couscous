class Solution:
    def checkInclusion(self, s1: str, s2: str) -> bool:
        l, r = 0, len(s1) - 1
        c1 = Counter(s1)

        while r < len(s2):
            c2 = Counter(s2[l:r+1])

            if c1 == c2:
                return True
            
            l += 1
            r += 1
        
        return False
