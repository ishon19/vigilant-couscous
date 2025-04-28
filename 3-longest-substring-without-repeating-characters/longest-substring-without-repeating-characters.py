class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        window = defaultdict(int)
        l, r = 0, 0
        res = 0

        while r < len(s):
            window[s[r]] += 1

            while window[s[r]] > 1:
                window[s[l]] -= 1
                l += 1

            res = max(res, r - l + 1)
            r += 1

        
        return res