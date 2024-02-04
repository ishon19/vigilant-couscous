class Solution:
    def minWindow(self, s: str, t: str) -> str:
        if not t: return ""
        
        hs, ht = {}, {}

        for c in t:
            ht[c] = ht.get(c, 0) + 1
        
        ls, lt = len(hs), len(ht)
        idx, minlen = [-1, -1], float("inf")

        l = 0
        for r in range(len(s)):
            current = s[r]
            hs[current] = hs.get(current, 0) + 1

            if current in ht and ht[current] == hs[current]:
                ls += 1
            
            while ls == lt:
                if r - l + 1 < minlen:
                    minlen = r - l + 1
                    idx = [l, r]
                
                hs[s[l]] -= 1

                if s[l] in ht and hs[s[l]] < ht[s[l]]:
                    ls -= 1
                
                l += 1
        
        l, r = idx
        return s[l:r+1] if minlen != float("inf") else ""
    