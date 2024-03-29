class Solution:
    def combinationSum2(self, candidates: List[int], target: int) -> List[List[int]]:
        candidates.sort()
        res = []
        
        def backtrack(idx, cur, target):
            if target == 0:
                # print(cur)
                res.append(list(cur))
            if target<=0:
                return
            
            prev = -1
            for i in range(idx, len(candidates)):
                if candidates[i] == prev:
                    continue
                cur.append(candidates[i])
                backtrack(i+1, cur, target - candidates[i])
                cur.pop()
                prev = candidates[i]
            
        backtrack(0, [], target)
        return res