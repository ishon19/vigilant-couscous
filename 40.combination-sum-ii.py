#
# @lc app=leetcode id=40 lang=python3
#
# [40] Combination Sum II
#

# @lc code=start
class Solution:
    def combinationSum2(self, candidates: List[int], target: int) -> List[List[int]]:
        candidates.sort()
        res = []
        path = []

        def dfs(idx, cur_sum):
            if cur_sum == target:
                res.append(path[:])
                return
            
            if idx not in range(len(candidates)) or cur_sum > target:
                return
            
            # at the same level we need to avoid repetition
            prev = -1
            for i in range(idx, len(candidates)):
                if candidates[i] == prev:
                    continue

                path.append(candidates[i])
                dfs(i+1, cur_sum + candidates[i])
                path.pop()
                prev = candidates[i]
        
        dfs(0, 0)
        return res
# @lc code=end

