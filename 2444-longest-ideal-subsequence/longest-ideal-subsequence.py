class Solution:
    def longestIdealString(self, s: str, k: int) -> int:
        # TLE
        # memo = {}

        # def dp(last, idx):
        #     if idx == len(s):
        #         return 0

        #     if (last, idx) in memo:
        #         return memo[(last, idx)]
            
        #     # Ignore current index
        #     ans = dp(last, idx + 1)
            
        #     # Include current index if it's valid
        #     if last == -1 or abs(ord(s[idx]) - last) <= k:
        #         ans = max(ans, 1 + dp(ord(s[idx]), idx + 1))
            
        #     memo[(last, idx)] = ans
        #     return ans
        
        # return dp(-1, 0)

        dp = [0] * 128
        for c in s:
            i = ord(c)
            dp[i] = max(dp[i-k:i+k+1]) + 1
        return max(dp)
