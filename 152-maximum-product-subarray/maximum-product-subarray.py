class Solution:
    def maxProduct(self, nums: List[int]) -> int:
        if not nums:
            return 0
        
        res = nums[0]
        curr_min = curr_max = 1

        for num in nums:
            temp = curr_min
            curr_min = min(num * curr_min, num * curr_max, num)
            curr_max = max(num, curr_max * num, temp * num)
            res = max(res, curr_max)
        
        return res
         