class Solution:
    def canPartition(self, nums: List[int]) -> bool:
        total = sum(nums)
        if total % 2 == 1:
            return False
        
        target = total // 2
        memo = {}

        def partitionHelper(index, currentTarget):
            if currentTarget == 0:
                return True
            
            if index == len(nums) or target < 0:
                return False
            
            if (index, currentTarget) in memo:
                return memo[(index, currentTarget)]
            
            result = partitionHelper(index + 1, currentTarget - nums[index]) or partitionHelper(index + 1, currentTarget)
            memo[(index, currentTarget)] = result
            return result
        
        return partitionHelper(0, target)