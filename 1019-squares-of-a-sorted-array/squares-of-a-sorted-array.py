class Solution:
    def sortedSquares(self, nums: List[int]) -> List[int]:
        # nums = [-x if x<0 else x for x in nums]
        # nums.sort()
        # return [x**2 for x in nums]

        # two pointer approach
        n = len(nums)
        l, r = 0, n - 1
        res = [0] * n
        for i in range(n-1,-1,-1):
            if abs(nums[l]) < abs(nums[r]):
                sq = nums[r]
                r -= 1
            else:
                sq = nums[l]
                l += 1
            res[i] = sq ** 2
        return res