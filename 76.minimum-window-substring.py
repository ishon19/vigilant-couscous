#
# @lc app=leetcode id=76 lang=python3
#
# [76] Minimum Window Substring
#

# @lc code=start
class Solution:
    def minWindow(self, s: str, t: str) -> str:
        t_count = defaultdict(int)
        s_count = defaultdict(int)

        for char in t:
            t_count[char] += 1

        res = ""
        min_len = len(s) + 1
        matches = 0
        left = 0

        for right in range(len(s)):
            char = s[right]
            s_count[char] += 1

            if s_count[char] <= t_count[char]:
                matches += 1
            
            left_char = s[left]
            while s_count[left_char] > t_count[left_char]:
                s_count[left_char] -= 1
                left += 1
                if left == len(s):
                    break
            
            if matches == len(t) and right - left + 1 < min_len:
                min_len = right - left + 1
                res = s[left:right+1]
        
        return res
# @lc code=end

