class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        
        cache = {}

        for i, num in enumerate(nums):
            if target - num in cache:
                return [i, cache[target-num]]
            else:
                cache[num] = i
        
        return [-1,-1]