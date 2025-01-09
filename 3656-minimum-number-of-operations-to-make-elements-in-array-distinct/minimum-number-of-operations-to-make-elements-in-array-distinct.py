class Solution:
    def isDistinct(self, arr):
        return len(arr) == len(set(arr))

    def minimumOperations(self, nums: List[int]) -> int:
        # base case
        if self.isDistinct(nums):
            return 0
        
        if len(nums) < 3:
            return 1
        
        res = 0
        
        while nums:
            if not self.isDistinct(nums):
                res += 1
            nums = nums[3:]
        
        return res



        
