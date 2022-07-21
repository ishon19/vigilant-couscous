class Solution:
    def threeSum(self, nums: List[int]) -> List[List[int]]:
        ans = []
        nums.sort()
        
        for i in range(len(nums)):
            if i>0 and nums[i] == nums[i-1]:
                continue
            
            l,r = i+1, len(nums) - 1
            while l<r:
                if nums[i]+nums[l]+nums[r] <0:
                    l+=1
                elif nums[i]+nums[l]+nums[r]>0:
                    r-=1
                else:
                    ans.append([nums[i], nums[l], nums[r]])
                    l+=1
                    while nums[l-1] == nums[l] and l<r:
                        l+=1
        
        print(ans)
        return ans