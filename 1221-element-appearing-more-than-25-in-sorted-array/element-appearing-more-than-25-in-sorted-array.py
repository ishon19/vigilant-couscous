class Solution:
    def findSpecialInteger(self, arr: List[int]) -> int:
        counts = collections.Counter(arr)
        for k, v in counts.items():
            if v/len(arr) > 0.25:
                return k
        return -1