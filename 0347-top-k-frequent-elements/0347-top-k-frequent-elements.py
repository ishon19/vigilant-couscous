class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        counter = Counter(nums)
        res = []
        arr = sorted([[k, v] for k, v in counter.items()], key=lambda v:v[1], reverse=True)
        for key, val in arr:
            if len(res) == k:
                return res
            res.append(key)
        return res