class Solution:
    def construct2DArray(self, original: List[int], m: int, n: int) -> List[List[int]]:
        res = []
        if m * n == len(original):
            i, j = 0, n-1
            while len(res) != m:
                res.append(original[i:j+1])
                i += n
                j += n
        return res