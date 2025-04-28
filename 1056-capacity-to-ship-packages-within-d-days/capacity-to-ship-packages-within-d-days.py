class Solution:
    def shipWithinDays(self, weights: List[int], days: int) -> int:
        l, r = max(weights), sum(weights)

        def isFeasible(capacity):
            days_needed = 1
            curr = 0

            for weight in weights:
                if curr + weight > capacity:
                    days_needed += 1
                    curr = weight
                else:                
                    curr += weight

                if days_needed > days:
                    return False 
            return True
                

        while l <= r:
            mid = (l+r) // 2

            if isFeasible(mid):
                r = mid - 1
            else:
                l = mid + 1
        
        return l