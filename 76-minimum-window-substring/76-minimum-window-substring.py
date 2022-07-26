class Solution:
    def minWindow(self, s: str, t: str) -> str:
        # base case
        if t == "": return ""
        
        # start off with the hashmaps
        hs, ht = {}, {}
        
        # count all the characters in the second
        for c in t:
            ht[c] = 1 + ht.get(c, 0)
        
        # what we need is the number of characters we have 
        # in the ht hashmap
        have, need = 0, len(ht)
        res, minLen = [-1, -1], float("inf")
        
        # slide window
        l = 0
        for r in range(len(s)):
            # put characters in the other hashmap now
            c = s[r]
            hs[c] = 1 + hs.get(c, 0)
            
            # now since we are concerned about only the characters we have in ht
            # we ignore any other character for 'have' count, we compare the values 
            # for the same character in both hashmaps
            if c in ht and ht[c] == hs[c]:
                have += 1
            
            # now keep on decreasing the window and keep on recording the window lengths
            while have == need:
                if (r - l + 1)<minLen:
                    minLen = r-l+1
                    res = [l, r]
                # keep on popping the left character
                hs[s[l]] -= 1
                
                # decrease have only if character is in the hashmap
                # and gets lesser than what we require it to be
                # as if it's more it is still fine (can incl duplicate)
                if s[l] in ht and hs[s[l]] < ht[s[l]]:
                    have -= 1
                l += 1
                
        # return the results
        l, r = res
        return s[l:r+1] if minLen!=float("inf") else ""
                
        
        