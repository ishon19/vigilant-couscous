class Solution:
    def maxProduct(self, nums: List[int]) -> int:
        updatedArr = sorted([val-1 for val in nums], reverse=True)
        return updatedArr[0] * updatedArr[1]
