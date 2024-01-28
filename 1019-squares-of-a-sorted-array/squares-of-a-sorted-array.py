class Solution:
    def sortedSquares(self, nums: List[int]) -> List[int]:
        nums = [-x if x<0 else x for x in nums]
        nums.sort()
        return [x**2 for x in nums]