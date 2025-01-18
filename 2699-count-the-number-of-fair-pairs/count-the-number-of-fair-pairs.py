"""
[0,1,7,4,4,5]
[(0,0),(1,1),(4,3),(4,4),(5,5),(7,2)]
"""

class Solution:
    def countFairPairs(self, nums: List[int], lower: int, upper: int) -> int:
        nums.sort()

        def find_sum(less_than):
            l, r = 0, len(nums)-1
            res = 0

            while l <= r:
                val = nums[l] + nums[r]
                if val < less_than:
                    res += r - l
                    l += 1
                else:
                    r -= 1
            
            return res
        
        return find_sum(upper + 1) - find_sum(lower)