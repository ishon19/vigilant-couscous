class Solution:
    def minimumOperations(self, nums: List[int]) -> int:
        ops = 0
        start = 0

        while start < len(nums):
            remain = nums[start:]
            if len(remain) == len(set(remain)):
                return ops
            
            start += min(3, len(nums) - start)
            ops += 1
        
        return ops



        
