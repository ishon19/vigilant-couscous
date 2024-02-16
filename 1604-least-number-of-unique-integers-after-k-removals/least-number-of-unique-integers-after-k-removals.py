class Solution:
    def findLeastNumOfUniqueInts(self, arr: List[int], k: int) -> int:
        counts = sorted([[k, v] for k, v in collections.Counter(arr).items()], key=lambda x: x[1])
        curSum = 0
        for idx, ele in enumerate(counts):
            curSum += ele[1]
            if curSum > k:
                return len(counts) - idx
        
        # print('here', curSum, curIdx)

        return 0