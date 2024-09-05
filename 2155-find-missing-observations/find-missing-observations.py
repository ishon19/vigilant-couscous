"""
n + m observations
m observations left right now
mean * (n+m) = x + y

rolls = [3,2,4,3] mean = 4, n = 2

4 * (2 + 4) = x + 12 
24 - 12 = x
12 = x
[6, 6]
12 = 6 * 2 = 3 * 3 * 2
"""

class Solution:
    def missingRolls(self, rolls: List[int], mean: int, n: int) -> List[int]:
        def get_possible_list(val):
            if val > 6 * n or val <n:
                return []
            
            dist = val // n
            mod = val % n

            res = [dist] * n
            for i in range(mod):
                res[i] += 1
            return res

        return get_possible_list((mean * (len(rolls) + n)) - sum(rolls))