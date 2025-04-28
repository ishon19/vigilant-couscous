class Solution:
    def maxSubarraySumCircular(self, nums: List[int]) -> int:
        # important observation that a wrap around case in a subarray
        # is essentially excluding a chunk in the middle 
        if not nums:
            return 0
        
        total_sum = 0 
        cur_max = 0
        max_sum = nums[0]
        cur_min = 0
        min_sum = nums[0]

        for num in nums:
            total_sum += num

            cur_max = max(num, cur_max + num)
            cur_min = min(num, cur_min + num)

            max_sum = max(max_sum, cur_max)
            min_sum = min(min_sum, cur_min)
        
        if max_sum < 0:
            return max_sum 
        
        return max(max_sum, total_sum - min_sum)
        


        