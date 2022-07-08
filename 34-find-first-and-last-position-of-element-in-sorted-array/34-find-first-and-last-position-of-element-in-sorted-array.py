class Solution:
    def searchRange(self, nums: List[int], target: int) -> List[int]:
        # calls for binary search
        # sorted, finding target 
        if len(nums) == 1:
            if nums[0] == target:
                return [0] * 2
            
        l, r = 0, len(nums)-1
        ans = []            
            
        while l<=r:
            mid = (l+r)//2  
            print('mid', mid)
            if nums[mid] == target:
                ans.append(mid)
                break
            elif target>nums[mid]:
                l = mid+1
            else:
                r = mid-1  
        
        # print(l,r)
        while l<=r:
            if nums[l] == target:
                ans.append(l)
            if nums[r] == target:
                ans.append(r)
            l+=1
            r-=1
        
        if len(ans) == 0:
            ans = [-1,-1]
        elif len(ans) == 1:
            ans = [ans[0]] * 2           
        
        return [min(ans), max(ans)]