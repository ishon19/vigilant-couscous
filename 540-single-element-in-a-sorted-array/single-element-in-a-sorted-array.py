"""
The pairs on left of single element
and on the right of the single element
have the digits in flipped odd/even position
eg:
 0 1 2 3 4 5 6 7 8 9
[1,1,2,2,3,4,4,5,6,6]
"""

class Solution:
    def singleNonDuplicate(self, nums: List[int]) -> int:
        l, r, res = 0, len(nums)-1, -1

        def isFeasible(idx):
            # check if the number is to 
            # the left of current idx
            if idx == len(nums) - 1:
                return True
            elif idx % 2 == 0:
                return nums[idx] != nums[idx+1]
            else:
                return nums[idx] != nums[idx-1]

        while l<=r :
            mid = (l+r)//2
            if isFeasible(mid):
                res = mid
                r = mid - 1
            else:
                l = mid + 1
        
        return nums[res]