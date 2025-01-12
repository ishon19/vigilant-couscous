class Solution:
    def longestConsecutive(self, nums: List[int]) -> int:
        num_set = set(nums)
        seen = set()
        res = 0

        for num in num_set:
            streak = 0
            curr = num
            if curr in seen:
                continue

            while curr in num_set:
                seen.add(curr)
                streak += 1
                curr += 1
            res = max(res, streak)
        
        return res
