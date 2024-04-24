class Solution:
    def tribonacci(self, n: int) -> int:
        if n == 0: return 0
        if n <=2: return 1
        a, b, c = 0, 1, 1
        for i in range(n-2): a, b, c = b, c, a +b+c
        return c

        # dp = [0] * (n + 1)
        # dp[1] = 1
        # dp[2] = 1
        
        # for i in range(3, n+1):
        #     dp[i] = dp[i-1] + dp[i-2] + dp[i-3]
        
        # return dp[-1]
#         memo = {}
        
#         def helper(num):
#             if num == 0:
#                 memo[num] = 0
#                 return memo[num]
#             if num <= 2: 
#                 memo[num] = 1
#                 return memo[num]
            
#             memo[num] = helper(num-1) + helper(num-2) + helper(num-3)
#             return memo[num]
        
#         return helper(n)