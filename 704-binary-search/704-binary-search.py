class Solution:
    def search(self, nums: List[int], target: int) -> int:
        l, r = 0, len(nums) - 1
        nums.sort()
        while l<=r:
            mid = (r+l)//2
            print(mid)
            if target == nums[mid]: return mid
            elif nums[mid]<target: l = mid + 1
            else: r = mid - 1
        return -1