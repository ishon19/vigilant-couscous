class Solution:
    def climbStairs(self, n: int) -> int:
        @cache
        def climb(steps):
            if steps >= 0:
                if steps == 0 or steps == 1:
                    return 1
                
                return climb(steps-1) + climb(steps-2)
        return climb(n)