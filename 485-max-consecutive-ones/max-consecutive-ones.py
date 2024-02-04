class Solution:
    def findMaxConsecutiveOnes(self, nums: List[int]) -> int:
        res = ans = 0
        for num in nums:
            res = res + 1 if num ^ 0 else 0 
            ans = max(ans, res)
        return ans