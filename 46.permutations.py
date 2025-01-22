#
# @lc app=leetcode id=46 lang=python3
#
# [46] Permutations
#

# @lc code=start
class Solution:
    def permute(self, nums: List[int]) -> List[List[int]]:
        res = []
        path = []
        seen = set()

        def dfs():
            if len(path) == len(nums):
                res.append(path[:])
                return
            
            for num in nums:
                if num not in seen:
                    seen.add(num)
                    path.append(num)
                    dfs()
                    path.pop()
                    seen.remove(num)
        
        dfs()
        return res
        
# @lc code=end

