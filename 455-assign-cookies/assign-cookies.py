class Solution:
    def findContentChildren(self, g: List[int], s: List[int]) -> int:
        res = 0
        s.sort()
        for greed in g:
            for i in range(len(s)):
                if s[i] >= greed:
                    del s[i]
                    res += 1
                    break
        return res