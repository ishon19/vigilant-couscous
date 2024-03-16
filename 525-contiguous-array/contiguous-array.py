class Solution:
    def findMaxLength(self, nums: List[int]) -> int:
        nums = [-1 if i == 0 else i for i in nums]
        cache = {0: -1}
        res = 0
        cur = 0

        for i in range(len(nums)):
            cur += nums[i]
            if cur in cache:
                res = max(res, i - cache[cur])
            else:
                cache[cur] = i
        return res