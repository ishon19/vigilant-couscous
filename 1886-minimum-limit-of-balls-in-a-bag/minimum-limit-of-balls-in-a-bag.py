class Solution:
    def minimumSize(self, nums: List[int], maxOperations: int) -> int:
        l, r = 1, max(nums)
        while l < r:
            mid = (l + r) // 2
            if sum((balls - 1) // mid for balls in nums) > maxOperations:
                l = mid + 1
            else:
                r = mid
        return l