class Solution:
    def lengthOfLIS(self, nums: List[int]) -> int:        
        # if not nums:
        #     return 0
        # tails = [0] * len(nums)
        # size = 0

        # for x in nums:
        #     l, r = 0, size
        #     while l != r:
        #         m = (l + r) // 2
        #         if tails[m] < x:
        #             l = m + 1
        #         else:
        #             r = m
        #     tails[l] = x
        #     size = max(l + 1, size)

        # return size
        # let dp[i] be the length of the LIS ending at i
        n = len(nums)
        dp = [1] * n

        for i in range(1, n):
            for j in range(i):
                if nums[i] > nums[j]:
                    dp[i] = max(dp[i], 1 + dp[j])
        
        return max(dp)

