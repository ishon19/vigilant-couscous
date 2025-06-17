class Solution:
    def minimizeMax(self, nums: List[int], p: int) -> int:
        nums.sort()

        def isFeasible(diff):
            i = 0
            count = 0

            while i < len(nums) - 1:
                if nums[i+1] - nums[i] <= diff:
                    count += 1
                    i += 2
                else:
                    i += 1
            
            return count >= p

        left, right = 0, max(nums) - min(nums)
        res = right

        while left <= right:
            mid = (left + right) // 2

            if isFeasible(mid):
                res = mid
                right = mid - 1
            else:
                left = mid + 1
        
        return res
