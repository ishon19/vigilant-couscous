class Solution:
    def minWindow(self, s1: str, s2: str) -> str:
        l1, l2 = len(s1), len(s2)
        min_window = inf

        i1, i2 = 0, 0
        res = ""

        while i1 < l1:
            if s1[i1] == s2[i2]:
                i2 += 1
                # if we've hit the end of the substring we're checking for
                # now would be time to evaluate if we have the complete thing
                # by going back 
                if i2 == l2:
                    l, r = i1, i1
                    i2 -= 1
                    while i2 >= 0:
                        if s1[l] == s2[i2]:
                            i2 -= 1
                        l -= 1
                    l += 1
                    if r - l < min_window:
                        min_window = r - l
                        res = s1[l:r+1]
                    i1 = l
                    i2 = 0
            i1 += 1
        
        return res