class Solution:
    def containsNearbyDuplicate(self, nums: List[int], k: int) -> bool:
        cache = defaultdict(list)

        for i, num in enumerate(nums):
            if num in cache:
                if abs(i - cache[num][-1]) <= k:
                    return True
            cache[num].append(i)
        
        return False