class Solution:
    def thirdMax(self, nums: List[int]) -> int:
        first = second = third = float("-inf")
        nums = list(set(nums))
        if len(nums) == 1:
            return nums[0]
        elif len(nums) == 2:
            return max(nums[0], nums[1])        
        for num in nums:
            if num>first:
                third = second
                second = first
                first = num
            elif num>second:
                third = second
                second = num
            elif num>third:
                third = num
        
        return third