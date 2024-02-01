class Solution:
    def divideArray(self, nums: List[int], k: int) -> List[List[int]]:
        if len(nums) < 3:
            return []

        nums.sort()
        res = []

        i, j = 0, 2
        while j < len(nums):
            a,b,c = nums[i], nums[i+1], nums[i+2]
            if abs(a-b) <= k and abs(b-a) <= k and abs(c-a) <= k:
                res.append(nums[i: j+1])
                i = j + 1
                j += 3
            else:
                return []
        
        return res
[1, 2, 3, 3, 3, 7]