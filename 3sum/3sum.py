class Solution:
    def threeSum(self, nums: List[int]) -> List[List[int]]:
        nums.sort()
        res = []
        
        for i in range(len(nums)):
            # avoid duplicates for the first number
            if i > 0 and nums[i] == nums[i-1]:
                continue
            
            target = -nums[i]            
            l, r = i + 1, len(nums) - 1
            
            while l < r:
                cur = nums[l] + nums[r]                
                if cur == target:
                    res.append([nums[i], nums[l], nums[r]])                
                    # avoid duplicates for second and third numbers
                    while l < r and nums[l] == nums[l+1]:
                        l += 1
                    while l < r and nums[r] == nums[r-1]:
                        r -= 1                
                    l += 1
                    r -= 1

                elif cur < target:
                    l += 1
                else:
                    r -= 1
        return res
                    
                