class Solution:
    def containsNearbyDuplicate(self, nums: List[int], k: int) -> bool:
        hm = {}

        for i, num in enumerate(nums):
            if nums[i] in hm:
                if abs(hm[nums[i]] - i) <= k:
                    return True
                hm[nums[i]] = i
            else:
                hm[nums[i]] = i
        
        return False