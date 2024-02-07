class Solution:
    def frequencySort(self, s: str) -> str:
        counts = collections.Counter(s)
        items = sorted(counts.items(), key=lambda x:x[1], reverse=True)
        res = ''
        for k, v in items:
            res += k * v
        return res

