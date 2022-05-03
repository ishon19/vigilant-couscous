class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        r,l,ans = 0,0,0
        chars = [0] * 128
        
        while r<len(s):
            chars[ord(s[r])] += 1
            
            # if it repeats then move the left pointer
            while chars[ord(s[r])]>1:
                chars[ord(s[l])] -= 1
                l += 1                        
            ans=max(ans, r-l+1)
            
            # no repetition, move ahead
            r+=1
        
        return ans