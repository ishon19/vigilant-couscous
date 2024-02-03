class Solution:
    def maxSumAfterPartitioning(self, arr: List[int], k: int) -> int:
        memo = {}

        def helper(idx):
            if idx in memo:
                return memo[idx]

            if idx >= len(arr):
                return 0
            
            curMax = 0
            val = 0

            for i in range(idx, min(len(arr), idx + k)):
                curMax = max(curMax, arr[i])
                val = max(val, curMax * (i - idx + 1) + helper(i + 1))
            
            memo[idx] = val
            return memo[idx]
        
        return helper(0)