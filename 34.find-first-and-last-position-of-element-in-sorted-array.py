#
# @lc app=leetcode id=34 lang=python3
#
# [34] Find First and Last Position of Element in Sorted Array
#

# @lc code=start
class Solution:
    def searchRange(self, nums: List[int], target: int) -> List[int]:
        def search(isFirst=True):
            l, r = 0, len(nums) - 1
            res = -1

            while l <= r:
                mid = (l + r) // 2

                if nums[mid] == target:
                    res = mid
                    if isFirst:
                        r = mid - 1
                    else:
                        l = mid + 1
                elif nums[mid] > target:
                    r = mid - 1
                else:
                    l = mid + 1

            return res
        
        return [search(isFirst=True), search(isFirst=False)]

    def searchRange(self, nums: List[int], target: int) -> List[int]:
        def binary_search(is_first=False):
            l, r = 0, len(nums) - 1
            res = -1 
            
            while l <= r:
                mid = (l + r) // 2
                
                if nums[mid] == target:
                    
# @lc code=end

