#
# @lc app=leetcode id=9 lang=python3
#
# [9] Palindrome Number
#

# @lc code=start
class Solution:
    def isPalindrome(self, x: int) -> bool:
        if x < 0:
            return False 

        rev = 0
        check = x

        while check:
            rev = rev * 10 + check % 10
            check = check // 10
        
        return rev == x

# @lc code=end

