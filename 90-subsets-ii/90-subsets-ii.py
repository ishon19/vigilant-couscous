class Solution:
    def subsetsWithDup(self, nums: List[int]) -> List[List[int]]:
        res = []
        nums.sort()
        
        def backtrack(idx, cur):
            if idx == len(nums):
                res.append(cur[::])
                return

            # subsets including the current number
            cur.append(nums[idx])
            backtrack(idx+1, cur)
            cur.pop()

            # subsets which do not include the current number
            # but also keep track of the duplicity - no two duplicate numbers should form the same subset
            while idx + 1 < len(nums) and nums[idx] == nums[idx+1]:
                idx += 1
            backtrack(idx + 1, cur)
        
        backtrack(0,[])
        return res