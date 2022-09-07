class Solution:
    def permute(self, nums: List[int]) -> List[List[int]]:
        ans = []
        
        # if just one element, return the deep copied version
        if len(nums) == 1:
            return [nums[:]]
        
        for i in range(len(nums)):
            # pop the first element off the array
            n = nums.pop(0)
            
            # recursively permutate over rest of the elements
            perms = self.permute(nums)
            
            # backtrack at this point
            for perm in perms:
                perm.append(n)
            
            ans.extend(perms)
            
            # add the removed element
            nums.append(n)
        return ans
            
            