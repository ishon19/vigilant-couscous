class Solution:
    def __init__(self):
        self.memo = {}
    
    def helper(self, amount):
        if amount == 0:
            return 0
        if amount < 0:
            return inf
        if amount in self.memo:
            return self.memo[amount]
        
        result = inf
        for coin in self.coins:
            result = min(result, 1 + self.helper(amount - coin))
        
        self.memo[amount] = result
        return result


    def coinChange(self, coins: List[int], amount: int) -> int:
        self.coins = coins
        res = self.helper(amount)
        return res if res!=inf else -1
