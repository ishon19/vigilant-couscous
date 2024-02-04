class Solution:
    def findMaxConsecutiveOnes(self, nums: List[int]) -> int:
        res = ans = 0
        for i in range(len(nums)):
            res = res + 1 if nums[i] ^ 0 else 0 
            ans = max(ans, res)
        return ans