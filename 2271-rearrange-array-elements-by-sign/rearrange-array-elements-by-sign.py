class Solution:
    def rearrangeArray(self, nums: List[int]) -> List[int]:
        res = [-1] * len(nums)
        pos = [i for i in nums if i>0]
        neg = [i for i in nums if i<0]

        j = k = 0
        for i in range(1, len(res)+1):
            if i%2:
                res[i-1] = pos[j]
                j += 1
            else:
                res[i-1] = neg[k]
                k += 1
        
        return res
