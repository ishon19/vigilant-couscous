class Solution:
    def change(self, amount: int, coins: List[int]) -> int:
        memo = {}

        def helper(index, remaining):
            if remaining == 0:
                return 1
            if remaining < 0 or index == len(coins):
                return 0
                
            if (index, remaining) in memo:
                return memo[(index, remaining)]
            
            memo[(index, remaining)] = helper(index, remaining - coins[index]) + helper(index + 1, remaining)
            return memo[(index, remaining)]
        
        return helper(0, amount)