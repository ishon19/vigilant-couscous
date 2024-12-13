class Solution:
    def shipWithinDays(self, weights: List[int], days: int) -> int:
        # check if a magical capacity of x can be shipped in `days` days
        def isFeasible(capacity):
            count = 1
            total = 0

            for weight in weights:
                if total + weight > capacity:
                    count += 1
                    total = weight
                else:
                    total += weight
            
            return count
        
        l, r  = max(weights), sum(weights)
        while l <= r:
            mid = (l + r) // 2            
            if isFeasible(mid) > days:
                l = mid + 1
            else:
                r = mid - 1 
        
        return l
