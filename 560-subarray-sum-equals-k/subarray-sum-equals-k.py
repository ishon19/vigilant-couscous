class Solution:
    def subarraySum(self, nums: List[int], k: int) -> int:
        # if(len(nums) == 1):
        #     return 1 if nums[0] == k else 0

        # pre = []
        # s = 0
        # for i in range(len(nums)):
        #     s += nums[i]
        #     pre.append(s)
        # pre = [0] + pre
        # res = 0
        
        # for i in range(1, len(pre)):
        #     if pre[i]-k in pre[:i]:
        #         res += 1
        
        # return res

        # prefix sum approach
        hm = {0: 1}
        cumsum = 0
        res = 0

        for num in nums:
            cumsum += num
            if cumsum - k in hm:
                res += hm[cumsum - k]
            hm[cumsum] = hm.get(cumsum, 0) + 1
        
        return res