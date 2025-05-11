class Solution:
    def threeConsecutiveOdds(self, arr: List[int]) -> bool:
        l = 0 

        while l < len(arr):
            streak = 0
            while l < len(arr) and arr[l] % 2 != 0:
                streak += 1
                if streak == 3:
                    return True
                l += 1
            l += 1

        return False