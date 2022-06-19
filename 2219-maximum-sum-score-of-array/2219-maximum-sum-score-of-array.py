class Solution:
    def maximumSumScore(self, nums: List[int]) -> int:
        cur_score = float("-inf")
        best_score = float("-inf")
        prefix_arr, prefix_rev_arr = [0]*len(nums), [0]*len(nums)
        prefix_arr[0] = nums[0]
        for i in range(1, len(nums)):
            prefix_arr[i] = prefix_arr[i-1] + nums[i]
        
        nums.reverse()
        
        prefix_rev_arr[0] = nums[0]
        for i in range(1, len(nums)):
            prefix_rev_arr[i] = prefix_rev_arr[i-1] + nums[i]
        
        
        for i in range(len(nums)):
            cur_score = max(prefix_arr[i], prefix_rev_arr[i])            
            best_score = max(best_score, cur_score)
        return best_score