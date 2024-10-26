class Solution:
    def findMissingRanges(self, nums: List[int], lower: int, upper: int) -> List[List[int]]:
        res = []
        prev = lower - 1

        for num in nums:
            if num - prev > 1:
                res.append([prev + 1, num - 1])
            prev = num

        if upper - prev > 0:
            res.append([prev + 1, upper])

        return res
