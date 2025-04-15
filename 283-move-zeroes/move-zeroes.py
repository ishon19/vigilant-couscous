class Solution:
    def moveZeroes(self, nums: List[int]) -> None:
        """
        Do not return anything, modify nums in-place instead.
        """
        nonZero = [num for num in nums if num != 0]
        for i, num in enumerate(nonZero):
            nums[i] = num
        
        if len(nonZero) < len(nums):
            for i in range(len(nonZero), len(nums)):
                nums[i] = 0
