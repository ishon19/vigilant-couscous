#
# @lc app=leetcode id=76 lang=python3
#
# [76] Minimum Window Substring
#

# @lc code=start
class Solution:
    def minWindow(self, s: str, t: str) -> str:
        if not s or not t:
            return ""
        
        need = {}
        for c in t:
            need[c] = need.get(c, 0) + 1
        
        have = {}
        required = len(need)
        left = 0
        current = 0
        res = ""
        minlen = float("inf")

        for right, char in enumerate(s):
            have[char] = have.get(char, 0) + 1 

            if char in need and have[char] == need[char]:
                current += 1
            
            while current == required:
                if right - left + 1 < minlen:
                    minlen = right - left + 1
                    res = s[left:right+1]

                exclude = s[left]
                have[exclude] -= 1

                if exclude in need and have[exclude] < need[exclude]:
                    current -= 1
                left += 1
        
        return res

# @lc code=end

