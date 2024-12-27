class Solution:
    def maxScoreSightseeingPair(self, values: List[int]) -> int:
        res = 0
        max_i = values[0] + 0

        for j in range(1, len(values)):
            cur = max_i + values[j] - j
            res = max(res, cur)
            max_i = max(max_i, values[j] + j)
        
        return res