class Solution:
    def maxSubArray(self, nums: List[int]) -> int:
        res = max_so_far = nums[0]

        for num in nums[1:]:
            max_so_far = max(max_so_far + num, num)
            res = max(res, max_so_far)
        
        return res