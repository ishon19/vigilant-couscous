class Solution:
    def getWinner(self, arr: List[int], k: int) -> int:
        streak = 0
        curr = arr[0]
        maxx = max(arr)

        for num in arr[1:]:
            opponent = num
            if curr > opponent:
                streak += 1
            else:
                curr = opponent
                streak = 1
            
            if streak == k or curr == maxx:
                return curr