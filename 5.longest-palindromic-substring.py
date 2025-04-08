#
# @lc app=leetcode id=5 lang=python3
#
# [5] Longest Palindromic Substring
#

# @lc code=start
class Solution:
    def longestPalindrome(self, s: str) -> str:
        # we can try expanding around the center to find the max
        # palindrome
        def expand_around_center(a, b): 
            i, j = a, b

            while i >=0 and j < len(s) and s[i] == s[j]:
                i -= 1
                j += 1
            
            return s[i+1:j]
        
        res = ""
        for i in range(len(s)):
            p1 = expand_around_center(i,i)
            p2 = expand_around_center(i,i+1)
            res = max(res, p1, p2, key=len)
        
        return res
            
# @lc code=end

