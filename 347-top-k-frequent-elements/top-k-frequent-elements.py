class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        buckets = [[] for _ in range(len(nums) + 1)]
        counts = Counter(nums)
        res = []

        for key, value in counts.items():
            buckets[value].append(key)
        
        for i in range(len(nums), -1, -1):
            res.extend(buckets[i])

            if len(res) >= k:
                return res[:k]
        
        return res
        

