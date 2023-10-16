class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        counter = Counter(nums)
        res = []
        arr = [[k, v] for k, v in counter.items()]
        arr = sorted(arr, key=lambda v:v[1], reverse=True)
        print(arr)
        for key, val in arr:
            print(key, val)
            if len(res) == k:
                return res
            res.append(key)
        return res