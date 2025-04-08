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
        
        res = ""
        count_t = defaultdict(int)
        count_s = defaultdict(int)

        for char in t:
            count_t[char] += 1
        
        min_length = len(s) + 1
        left = 0
        matches = 0

        for right in range(len(s)):
            # expand the window by adding the character to the right
            count_s[s[right]] += 1

            if count_s[s[right]] <= count_t[s[right]]:
                matches += 1
            
            # shrink the window from left if possible 
            while count_s[s[left]] >= count_t[s[left]]:
                count_s[s[left]] -= 1
                left += 1
            
            if matches == len(t) and right - left + 1 < min_length:
                min_length = right - left + 1
                res = s[left:right+1]
        
        return res
# @lc code=end

