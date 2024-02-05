class Solution:
    def firstUniqChar(self, s: str) -> int:
        hm = collections.Counter(s)
        for i, c in enumerate(s):
            if hm[c] == 1:
                return i
        return -1