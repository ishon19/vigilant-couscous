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
        dp = [1] * len(nums)
        for i in range(1, len(nums)):
            for j in range(i):
                if nums[i] > nums[j]:
                    dp[i] = max(dp[i], dp[j] + 1)
        return max(dp)

