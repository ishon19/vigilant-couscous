class Solution:
    def longestSubarray(self, nums: List[int]) -> int:
        max_so_far = res = streak = 0

        for num in nums:
            if max_so_far < num:
                max_so_far = num
                res = streak = 0

            if num == max_so_far:
                streak +=1
            else:
                streak = 0

            res = max(res, streak)

        return res         