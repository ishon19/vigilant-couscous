class Solution:
    def minimizedMaximum(self, n: int, quantities: List[int]) -> int:
        # find a number x which satisfies the conditions
        def isfeasible(x):
            i = 0
            remaining = quantities[i]

            for j in range(n):
                if remaining <= x:
                    i += 1                
                    if i == len(quantities):
                        return True
                    else:
                        remaining = quantities[i]
                else:
                    remaining -= x
            return False
        
        l, r = 0, max(quantities)

        while l < r:
            mid = (l+r)//2
            if isfeasible(mid):
                r = mid
            else:
                l = mid + 1
        
        return l