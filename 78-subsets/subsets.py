class Solution:
    def subsets(self, nums: List[int]) -> List[List[int]]:
        res = []

        def helper(idx, pattern):
            if idx <= len(nums): 
                if pattern not in res:
                    res.append(pattern)
                helper(idx + 1, pattern + [nums[idx] if idx < len(nums) else []])
                helper(idx + 1, pattern)
        
        helper(0, [])
        return res
            

            
