class Solution:
    def splitArray(self, nums: List[int], k: int) -> int:
        def isFeasible(x):
            # check how many subarrays are needed to satisfy this
            running_sum = 0
            count = 1

            for num in nums:
                if running_sum + num > x:
                    count += 1
                    running_sum = num
                else:
                    running_sum += num
            return count <= k

        l, r = max(nums), sum(nums)

        while l <= r:
            mid = (l + r) // 2

            if isFeasible(mid):
                r = mid - 1
            else:
                l = mid + 1
        
        return l