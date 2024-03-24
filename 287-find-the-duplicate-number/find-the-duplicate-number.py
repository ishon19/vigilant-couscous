class Solution:
    def findDuplicate(self, nums: List[int]) -> int:
        # TLE
        # for num in nums:
        #     idx = nums.index(num)
        #     if num in nums[idx+1:]:
        #         return num
        # return -1

        l, r = 1, len(nums) - 1

        while l<=r:
            mid = (l + r) // 2 
            count = sum(num <= mid for num in nums)

            if count>mid:
                dup = mid
                r = mid - 1
            else:
                l = mid + 1
        
        return dup
