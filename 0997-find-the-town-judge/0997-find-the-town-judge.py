class Solution:
    def findJudge(self, n: int, trust: List[List[int]]) -> int:
        if not trust and n==1:
            return 1
        
        cache = {}
        for a, b in trust:
            if b not in cache:
                cache[b] = [a]
            else:
                cache[b].append(a)
        print(cache)
        
        for k, v in cache.items():
            if len(cache[k]) == n-1:
                # check if k is present in someones trust list
                for vals in cache.values():
                    if k in vals:
                        return -1
                return k
        return -1
            