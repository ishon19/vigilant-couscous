class Solution:
    def minLength(self, s: str) -> int:
        l, r = 0, 1

        while "AB" in s or "CD" in s:
            if s[l:r+1] in ['AB', 'CD']:
                s = s[:l]+s[r+1:]
                # print('midway', s)
                l = 0
                r = 1
            else:
                l += 1
                r += 1
        
        return len(s)