class Solution:
    def combinationSum(self, candidates: List[int], target: int) -> List[List[int]]:
        ans = []
        
        def helper(remaining, currPattern, idx):            
            if remaining == 0:
                print(currPattern)
                ans.append(list(currPattern))
            elif remaining < 0:
                return
            
            for i in range(idx,len(candidates)):
                currPattern.append(candidates[i])
                helper(remaining - candidates[i], currPattern, i)
                currPattern.pop()
        
        helper(target, [], 0)
        
        return ans