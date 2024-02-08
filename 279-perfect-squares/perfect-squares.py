class Solution:
    def numSquares(self, n: int) -> int:
        perf = [ i**2 for i in range(1, int(math.sqrt(n))+1)]

        # def helper(num):
        #     if num in perf:
        #         return 1

        #     min_num = float("inf")

        #     for sq in perf:
        #         if num < sq:
        #             break
        #         temp = helper(num-sq) + 1
        #         min_num = min(min_num, temp)
        #     return min_num

        dp = [float("inf")] * (n + 1)

        # base case
        dp[0] = 0

        for i in range(1, n+1):
            for sq in perf:
                if i < sq:
                    break
                dp[i] = min(dp[i], dp[i-sq] + 1)
        return dp[-1]
        