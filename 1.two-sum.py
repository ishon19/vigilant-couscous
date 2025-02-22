#
# @lc app=leetcode id=1 lang=python3
#
# [1] Two Sum
#

# @lc code=start
class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        res = [-1, -1]
        sumMap = {}

        for i in range(len(nums)):
            if target - nums[i] in sumMap:
                return [i, sumMap[target - nums[i]]] 
            sumMap[nums[i]] = i

        return res        
# @lc code=end

