from typing import List 
class Solution:
    def maxProduct(self, nums: List[int]) -> int:
        if len(nums) == 0:
            return 0
        
        min_prd = nums[0]
        max_prd = nums[0]
        ans = max_prd
        
        for i in range(1, len(nums)):
            curr = nums[i]
            temp = max_prd
            max_prd = max(curr, temp * curr, min_prd * curr)
            min_prd = min(curr, temp * curr, min_prd * curr)
            ans = max(ans, max_prd)
        
        return ans