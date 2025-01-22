#
# @lc app=leetcode id=39 lang=python3
#
# [39] Combination Sum
#

# @lc code=start
class Solution:
    def combinationSum(self, candidates: List[int], target: int) -> List[List[int]]:
        res = []
        path = []

        def dfs(idx, current):
            if idx not in range(0, len(candidates)) or current > target:
                return
            
            if current == target:
                res.append(path[:])
                return
            
            path.append(candidates[idx])
            dfs(idx, current + candidates[idx])
            path.pop()
            dfs(idx+1, current)
        
        dfs(0,0)
        return res
# @lc code=end

