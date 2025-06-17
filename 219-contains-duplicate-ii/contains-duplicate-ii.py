class Solution:
    def containsNearbyDuplicate(self, nums: List[int], k: int) -> bool:
        seen = defaultdict(int)

        for i, num in enumerate(nums):
            if num in seen and abs(seen[num] - i) <= k:
                return True             
            seen[num] = i
        
        return False