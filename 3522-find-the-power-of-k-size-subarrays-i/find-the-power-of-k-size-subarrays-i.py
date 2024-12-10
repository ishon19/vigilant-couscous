class Solution:
    def resultsArray(self, nums: List[int], k: int) -> List[int]:
        l, r = 0, k-1
        res = []
        
        def isValid(arr):
            for i in range(len(arr)-1):
                if arr[i+1] - arr[i] != 1:
                    return False
            return True

        while r < len(nums):
            res.append(max(nums[l:r+1]) if isValid(nums[l:r+1]) else -1)
            l += 1
            r += 1
        
        return res
        