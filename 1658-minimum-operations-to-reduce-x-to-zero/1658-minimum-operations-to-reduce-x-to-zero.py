class Solution:
    def minOperations(self, nums: List[int], x: int) -> int:
        l,r,c,m,s = 0,0,0,-1,sum(nums)
        while r<len(nums):
            c += nums[r]
            while c > s-x and l<=r:
                c -= nums[l]
                l += 1
            if c == s-x:
                m = max(m, r-l+1)
            r += 1
        return len(nums) - m if m!=-1 else -1