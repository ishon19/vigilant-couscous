class Solution:
    def lengthOfLIS(self, nums: List[int]) -> int:        
        # def helper(idx, pattern):
        #     if idx == len(nums)-1:
        #         print(pattern)
        #         return len(pattern)
        #     if pattern and nums[idx] > pattern[-1]:
        #         pattern.append(nums[idx])            
        #     return helper(idx+1, pattern)
        # return helper(0, [])       
        if not nums:
            return 0
        dp = [nums[0]]
        for i in range(1, len(nums)):
            if nums[i] > dp[-1]:
                dp.append(nums[i])
            else:
                l, r = 0, len(dp) - 1
                while l < r:
                    mid = (l + r) // 2
                    if dp[mid] < nums[i]:
                        l = mid + 1
                    else:
                        r = mid
                dp[l] = nums[i]
        return len(dp)

