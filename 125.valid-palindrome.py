#
# @lc app=leetcode id=125 lang=python3
#
# [125] Valid Palindrome
#

# @lc code=start
class Solution:
    def isPalindrome(self, s: str) -> bool:
        cleanStr = [ch.lower() for ch in s if ch.isalnum()]

        l, r = 0, len(cleanStr)-1

        while l < r:
            if cleanStr[l] != cleanStr[r]:
                return False
            l += 1
            r -= 1

        return True
# @lc code=end

