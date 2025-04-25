#
# @lc app=leetcode id=5 lang=python3
#
# [5] Longest Palindromic Substring
#

# @lc code=start
class Solution:
    def longestPalindrome(self, s: str) -> str:

        def expand_around_center(i, j):
            while i >=0  and j < len(s) and s[i] == s[j]:
                i -= 1
                j += 1
            return s[i+1:j]

        
        res = ""
        for i, _ in enumerate(s):
            odd_length = expand_around_center(i, i)
            even_length = expand_around_center(i, i+1)
            res = max(res, odd_length, even_length, key=len)
        return res
            
# @lc code=end

