class Solution:
    def combinationSum4(self, nums: List[int], target: int) -> int:
        # if not nums:
            # return 0
        
        # nums.sort()
        # ans = []
        
        # def helper(currPattern, remaining, idx):
            # if remaining == 0:
                # ans.append(list(currPattern))
            # elif remaining<0:
                # return
            # else:
                # for i in range(idx, len(nums)):
                    # currPattern.append(nums[i])
                    # helper(currPattern, remaining - nums[i], idx)
                    # currPattern.pop()
        
        
        # helper([],target, 0)
        # # print(ans)
        # return len(ans)
        @lru_cache(None)
        def helper(remaining):
            if remaining == 0:
                return 1
            
            ans = 0
            for num in nums:
                if remaining - num >= 0:
                    ans += helper(remaining - num)
            return ans
        
        return helper(target)