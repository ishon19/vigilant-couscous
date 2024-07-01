class Solution:
    def threeConsecutiveOdds(self, arr: List[int]) -> bool:
        if len(arr) < 3:
            return False

        start, end = 0, 2
        res = False

        while end < len(arr):
            if all(num%2!=0 for num in arr[start: end+1]):
                res = True
            start += 1
            end += 1
        
        return res