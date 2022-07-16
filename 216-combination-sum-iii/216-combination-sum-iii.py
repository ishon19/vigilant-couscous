class Solution:
    def combinationSum3(self, k: int, n: int) -> List[List[int]]:
        ans = []
        nums = [i for i in range(1, 10)]
        
        def helper(currPattern, idx, remaining):
            if remaining < 0 or len(currPattern)> k:
                return
            elif remaining == 0 and len(currPattern) == k:
                ans.append(list(currPattern))
            else:
                for i in range(idx, len(nums)):
                    if nums[i] not in currPattern:
                        currPattern.append(nums[i])
                        helper(currPattern, i, remaining-nums[i])
                        currPattern.pop()
            
            return currPattern
        
        helper([], 0, n)
        return ans