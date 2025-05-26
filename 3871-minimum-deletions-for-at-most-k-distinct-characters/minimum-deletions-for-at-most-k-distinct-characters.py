class Solution:
    def minDeletion(self, s: str, k: int) -> int:
        counts = sorted([[counts, key] for key, counts in Counter(s).items()], key=lambda x: x[0])
        deletions = len(counts) - k
        res = 0
        for i in range(deletions):
            res += counts[i][0]
        return res