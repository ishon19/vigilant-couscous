class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        charMap = Counter()
        l, r = 0, 0
        res = 0

        while r < len(s):
            charMap[s[r]] += 1

            while charMap[s[r]] > 1:
                charMap[s[l]] -= 1
                l += 1
            
            res = max(res, r - l + 1)
            r += 1
        
        return res


        