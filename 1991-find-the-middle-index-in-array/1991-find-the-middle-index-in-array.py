class Solution:
    def findMiddleIndex(self, nums: List[int]) -> int:
        # based on prefix sum 
        leftSum = 0
        total = sum(nums)
        for idx, num in enumerate(nums):
            if leftSum == (total - leftSum - num):
                return idx
            leftSum += num
        return -1