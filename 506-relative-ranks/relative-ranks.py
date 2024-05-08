class Solution:
    def findRelativeRanks(self, score: List[int]) -> List[str]: 
        ranks = ['Gold Medal', 'Silver Medal', 'Bronze Medal'] + [str(i) for i in range(4, len(score) + 1)]
        rankMap = {s:r for s, r in zip(sorted(score, reverse=True), ranks)}
        res = [rankMap[s] for s in score]
        return res