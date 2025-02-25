#
# @lc app=leetcode id=739 lang=python3
#
# [739] Daily Temperatures
#

# @lc code=start
class Solution:
    def dailyTemperatures(self, temperatures: List[int]) -> List[int]:
        n = len(temperatures)
        stack = []
        res = [0] * n

        for idx, temperature in enumerate(temperatures):
            while stack and temperature > temperatures[stack[-1]]:
                prev_idx = stack.pop()
                res[prev_idx] = idx - prev_idx
            stack.append(idx)
        
        return res
# @lc code=end

