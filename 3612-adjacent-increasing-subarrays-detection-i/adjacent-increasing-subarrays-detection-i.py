class Solution:
    def hasIncreasingSubarrays(self, nums: List[int], k: int) -> bool:
        res = False
        def checkInc(arr):
            res = True
            for i in range(len(arr)-1):
                if arr[i] >= arr[i+1]:
                    return False
            return res

        for i in range(len(nums)):
            l, r = i, i + k - 1
            lastInc = False
            while r <len(nums):       
                # print(l,r, nums[l:r+1], checkInc(nums[l:r+1]))         
                if checkInc(nums[l:r+1]) and lastInc:
                    return True
                lastInc = checkInc(nums[l:r+1])
                l += k
                r += k
        return res
                