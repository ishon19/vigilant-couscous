#
# @lc app=leetcode id=128 lang=python3
#
# [128] Longest Consecutive Sequence
#

# @lc code=start
class Solution:
    def longestConsecutive(self, nums: List[int]) -> int:
        numSet = set(nums)
        seen = set()
        streak = 0

        for num in numSet:
            streak_from_here = 0

            if num in seen:
                continue

            curr = num
            while curr in numSet:
                seen.add(curr)
                streak_from_here += 1
                curr += 1
            streak = max(streak, streak_from_here)
        
        return streak


# @lc code=end

