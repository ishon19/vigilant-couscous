class Solution:
    def threeSumClosest(self, nums: List[int], target: int) -> int:
        nums.sort()
        res = float("inf")
        
        for i in range(len(nums)):
            if i > 0 and nums[i] == nums[i-1]:
                continue 
                
            l, r = i + 1, len(nums) - 1
            
            while l < r:
                total = nums[i] + nums[l] + nums[r]
                
                if abs(total - target) < abs(res - target):
                    res = total
                
                if total == target:
                    return total
                elif total < target:                    
                    l += 1
                else:
                    r -= 1

        return res