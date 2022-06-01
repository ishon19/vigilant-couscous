class Solution:
    def runningSum(self, nums: List[int]) -> List[int]:
        val = 0
        ans = []
        for i in nums:
            val += i
            ans.append(val)
        return ans