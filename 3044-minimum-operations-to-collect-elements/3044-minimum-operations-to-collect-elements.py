class Solution:
    def minOperations(self, nums: List[int], k: int) -> int:
        target = [i for i in range(1, k+1)]
        res = []
        ans = 0

        for num in nums[::-1]:
            if sorted(res) == target:
                break  
            if num in target and num not in res:
                res.append(num)
            ans += 1
        
        return ans

