# 27 Nov, 10.26 AM
class Solution:
    def searchRange(self, nums, target):
        res = [-1, -1]

        # for the first position find the leftmost element
        l, r = 0, len(nums) - 1
        pos = -1
        while l<=r:
            mid = (l+r)//2
            if nums[mid] == target:
                pos = mid
                r = mid - 1
            elif nums[mid] > target:
                r = mid - 1
            else:
                l = mid + 1
        res[0] = pos

        # for the second element find the rightmost element
        l, r = 0, len(nums) - 1
        pos = -1
        while l <= r:
            mid = (l+r) // 2
            if nums[mid] == target:
                pos = mid
                l = mid + 1
            elif nums[mid] > target:
                r = mid - 1
            else:
                l = mid + 1
        res[1] = pos
        
        return res

# class Solution:
#     def searchRange(self, nums: List[int], target: int) -> List[int]:
#         if len(nums)==1:
#             return [-1,-1] if nums[0] != target else [0,0]
#         res = [-1,-1]
#         l, r = 0, len(nums)-1
#         while l<=r:
#             mid = (l+r)//2
#             if nums[mid] == target:
#                 l,r = mid, mid
#                 while l>=0 or r<len(nums):
#                     if l>=0 and nums[l] == target:
#                         res[0] = l
#                     if r<len(nums) and nums[r] == target:
#                         res[1] = r
#                     l -= 1
#                     r += 1
#                 return res
#             elif nums[mid]>target:
#                 r = mid - 1
#             else:
#                 l = mid + 1
#         return res