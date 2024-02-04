class Solution:
    def findMaxConsecutiveOnes(self, nums: List[int]) -> int:
        res = 0
        ans = 0
        for i in range(len(nums)):
            val = nums[i] ^ 0
            if val:
                res += 1
            else:
                res = 0
            ans = max(ans, res)
        return ans