#
# @lc app=leetcode id=3 lang=python3
#
# [3] Longest Substring Without Repeating Characters
#

# @lc code=start
class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        charMap = {}
        start = 0
        res = 0

        for end, char in enumerate(s):
            if char in charMap and charMap[char] >= start:
                start = charMap[char] + 1
            
            charMap[char] = end
            res = max(res, end - start + 1)
        
        return res

# @lc code=end

