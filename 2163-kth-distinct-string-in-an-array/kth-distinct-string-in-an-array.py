class Solution:
    def kthDistinct(self, arr: List[str], k: int) -> str:
        counts = collections.Counter(arr)
        res = ''
        itr = 1
        for i in range(len(arr)):
            if counts[arr[i]] == 1:
                if itr == k:
                    return arr[i]
                itr += 1
        return res