class Solution:
    def findAnagrams(self, s: str, p: str) -> List[int]:
        hm = Counter(p)
        res = []
        l, r = 0, len(p)-1

        while r < len(s):
            if Counter(s[l:r+1]) == hm:
                res.append(l)
            l += 1
            r += 1
        
        return res