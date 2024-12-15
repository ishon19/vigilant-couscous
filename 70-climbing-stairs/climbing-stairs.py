class Solution:
    def climbStairs(self, n: int) -> int:
        @cache
        def helper(step):
            if step > n:
                return 0
            if step == n:
                return 1                        
            return helper(step + 1) + helper(step + 2)
        
        return helper(0)
            