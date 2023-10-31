class Solution:
    def sortByBits(self, arr: List[int]) -> List[int]:
        res = []
        for num in arr:
            ct = 0
            curr = num
            while num:
                ct += num % 2
                num = math.floor(num / 2)            
            res.append([curr, ct])
        res = sorted(res, key=lambda e: e[0])
        res = sorted(res, key=lambda e: e[1])
        final = [e[0] for e in res]
        return final