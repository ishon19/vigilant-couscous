class Solution:
    def lengthOfLongestSubstringKDistinct(self, s: str, k: int) -> int:
        l = ans = 0
        
        counter = {}
        
        for r in range(len(s)):            
            counter[s[r]] = counter.get(s[r], 0) + 1             
            
            if len(counter)<=k:
                ans = max(ans, r-l+1)
            else:
                counter[s[l]] -= 1
                if counter[s[l]] == 0:
                    counter.pop(s[l])
                l += 1
        
        return ans