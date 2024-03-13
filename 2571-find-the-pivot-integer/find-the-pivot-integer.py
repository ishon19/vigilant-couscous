class Solution:
    def pivotInteger(self, n: int) -> int:
        pref = list(itertools.accumulate(i for i in range(1, n+1)))
        suff = list(itertools.accumulate(i for i in range(n, 0, -1)))[::-1]
        for idx, (i, j) in enumerate(zip(pref, suff)):
            if i == j: return idx + 1
        return -1