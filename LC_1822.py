class Solution:
    def arraySign(self, nums: List[int]) -> int:
        if 0 in nums:
            return 0
        countNeg = 0
        for e in nums:
            if e<0:
                countNeg += 1
        return 1 if countNeg%2==0 else -1;