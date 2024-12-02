class Solution:
    def coinChange(self, coins: List[int], amount: int) -> int:
        @cache
        def min_change(total):
            if total == amount:
                return 0
            
            if total>amount:
                return inf
            
            res = inf
            for coin in coins:
                change = min_change(total + coin)
                if change == inf:
                    continue
                res = min(res, change + 1)
            return res
        ans = min_change(0)
        return ans if ans != inf else -1