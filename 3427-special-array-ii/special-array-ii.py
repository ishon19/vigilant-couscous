class Solution:
    def isArraySpecial(self, nums: List[int], queries: List[List[int]]) -> List[bool]:
        # store cumulative indices violating the constraint
        pref = [0] * len(nums)
        
        for i in range(1, len(nums)):            
                pref[i] = pref[i - 1] + 1 if nums[i] % 2 == nums[i-1] % 2 else pref[i - 1]
        
        res = []
        for query in queries:
            l, r = query
            res.append(pref[r] - pref[l] == 0)
        
        return res

        # Brute Force
        # res = []
        # def difference(num1, num2):
        #     return (num1 % 2 == 0 and num2 % 2 != 0) or (num1 % 2 != 0 and num2 % 2 ==0)
        # def checkParity(arr):
        #     isSpecial = True
        #     i = 0
        #     while i < len(arr)-1:
        #         isSpecial = isSpecial and difference(arr[i], arr[i+1])
        #         i += 1
        #     return isSpecial
        # for query in queries:
        #     l, r = query
        #     res.append(checkParity(nums[l:r+1]))
        # return res