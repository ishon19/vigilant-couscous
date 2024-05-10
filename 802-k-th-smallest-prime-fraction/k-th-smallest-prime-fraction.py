class Solution:
    def kthSmallestPrimeFraction(self, arr: List[int], k: int) -> List[int]:
        res = [0, 0]
        pairs = []
        for i in range(len(arr)):
            for j in range(i, len(arr)):
                pairs.append([arr[i], arr[j], arr[i]/arr[j]])  
        kth = sorted(pairs, key=lambda x: x[2])[k-1]
        res = [kth[0], kth[1]]
        return res