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

        need = Counter(t)

        left = 0
        min_len = float("inf")
        min_left = 0
        still_needed = len(t)

        for right, char in enumerate(s):
            if char in need:
                need[char] -= 1
                if need[char] >= 0:
                    still_needed -= 1

            while still_needed == 0:
                if right - left + 1 < min_len:
                    min_len = right - left + 1
                    min_left = left

                left_char = s[left]
                if left_char in need:
                    need[left_char] += 1
                    if need[left_char] > 0:
                        still_needed += 1
                left += 1
        
        return "" if min_len == float("inf") else s[min_left:min_left+min_len]

# @lc code=end

