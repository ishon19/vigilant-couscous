class Solution:
    def minDays(self, bloomDay: List[int], m: int, k: int) -> int:
        # Since we have `bloomDay` flowers
        # anything less than m * k would be infeasible
        if m * k > len(bloomDay):
            return -1

        def isFeasible(day):
            bouquets = 0
            consecutive = 0

            for d in bloomDay:
                if d <= day:
                    consecutive += 1
                    if consecutive == k:
                        bouquets += 1
                        consecutive = 0
                else:
                    consecutive = 0

            return bouquets >= m
        

        left, right = min(bloomDay), max(bloomDay)
        
        while left <= right:
            mid = (left + right) // 2

            if isFeasible(mid):
                right = mid - 1
            else:
                left = mid + 1
        
        return left