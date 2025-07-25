#
# @lc app=leetcode id=162 lang=python3
#
# [162] Find Peak Element
#

# @lc code=start
class Solution:
    def findPeakElement(self, nums: List[int]) -> int:
        l, r = 0, len(nums)-1
        
        while l < r:
            mid = (l + r) // 2
            
            if nums[mid] > nums[mid+1]:
                r = mid
            else:
                l = mid + 1
        
        return l

    def findValleyElement(self, nums: List[int]) -> int:
        l, r = 0, len(nums) - 1
        
        while l < r:
            mid = (l + r) // 2
            
            if nums[mid] > nums[mid+1]:
                l = mid + 1
            else:
                r = mid
        
        return l


if __name__ == "__main__":
    sol = Solution()
    index = sol.findValleyElement([3,2,9])
    assert index == 1

# @lc code=end

