class Solution:
    def countPairs(self, nums: List[int], target: int) -> int:
        res = 0
        
        for i in range(len(nums)):
            for j in range(len(nums)):
                if i != j and i<j and nums[i] + nums[j] < target:
                    res += 1
        
        return res
                