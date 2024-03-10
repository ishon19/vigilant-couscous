class Solution:
    def maximumHappinessSum(self, happiness: List[int], k: int) -> int:
        happiness.sort(reverse=True)
        res = 0

        for i in range(k):
            val = happiness[i]
            res += max(0, val - i)
        
        return res
