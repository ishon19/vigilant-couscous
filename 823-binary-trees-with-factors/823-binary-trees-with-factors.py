class Solution:
    def numFactoredBinaryTrees(self, arr: List[int]) -> int:
        mod = 10 ** 9 + 7
        arr.sort()
        dp = [1] * (len(arr))
        
        hashmap = {v:k for k, v in enumerate(arr)}
        
        for i, v in enumerate(arr):
            for j in range(i):
                if v % arr[j] == 0:
                    right = v/arr[j]
                    if right in hashmap:
                        dp[i] += dp[j] * dp[hashmap[right]]
                        dp[i] %= mod
        
        return sum(dp)% mod