class Solution:
    def productExceptSelf(self, nums: List[int]) -> List[int]:
        l, r = 1, 1
        ans = [0] * len(nums)
        
        for i in range(len(nums)):
            ans[i] = l
            l *= nums[i]
        
        for j in reversed(range(len(nums))):
            ans[j] *= r
            r *= nums[j]
        
        print(ans)
        return ans