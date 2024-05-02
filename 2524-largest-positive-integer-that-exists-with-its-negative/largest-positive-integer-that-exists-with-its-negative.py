class Solution:
    def findMaxK(self, nums: List[int]) -> int:
        res = -sys.maxsize
        for num in nums:
            if -num in nums:
                res = max(res, abs(num))
        return -1 if res == -sys.maxsize else res