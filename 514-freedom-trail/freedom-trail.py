class Solution:
    def findRotateSteps(self, ring: str, key: str) -> int:        
        
        # rather than a dfs go specifically to the indices where a character could be
        idxMap = collections.defaultdict(list)
        for i, k in enumerate(ring):
            idxMap[k].append(i)
        
        memo = {}

        def helper(rIdx, kIdx):
            if kIdx == len(key):
                return 0
            
            if (rIdx, kIdx) in memo:
                return memo[(rIdx, kIdx)]
            
            res = sys.maxsize
            for nextIdx in idxMap[key[kIdx]]:
                clock = abs(nextIdx - rIdx)
                anti = len(ring) - clock
                step = min(clock, anti)
                res = min(res, 1 + step + helper(nextIdx, kIdx + 1))
            
            memo[(rIdx, kIdx)] = res
            return res
        
        return helper(0, 0)

