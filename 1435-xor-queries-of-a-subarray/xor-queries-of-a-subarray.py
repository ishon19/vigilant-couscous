class Solution:
    def xorQueries(self, arr: List[int], queries: List[List[int]]) -> List[int]:
        pre = [0]

        for num in arr:
            pre.append(pre[-1] ^ num)

        res = [pre[r + 1] ^ pre[l] for l, r in queries]
        return res
                