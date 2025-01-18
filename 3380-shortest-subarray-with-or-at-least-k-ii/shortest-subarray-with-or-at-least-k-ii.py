class Solution:
    def minimumSubarrayLength(self, nums: List[int], k: int) -> int:
        dp = {}
        res = float('inf')
        for num in nums:
            next_dp = {}
            # Start new subarray with num
            new_val = num
            new_len = 1
            next_dp[new_val] = new_len
            if new_val >= k:
                res = min(res, new_len)
            for val, length in dp.items():
                new_val = val | num
                new_len = length + 1
                if new_val not in next_dp or new_len < next_dp[new_val]:
                    next_dp[new_val] = new_len
                    if new_val >= k:
                        res = min(res, new_len)
            dp = next_dp
        return res if res != float('inf') else -1
