from typing import List

class Solution:
    def helper(self, nums: List[int]) -> int:
        t1, t2 = 0, 0 
        
        for n in nums:
            x = max(t1+n, t2)
            t1 = t2
            t2 = x
        return t2
        
    def rob(self, nums: List[int]) -> int:
        return max(nums[0], self.helper(nums[1:]), self.helper(nums[:-1]))