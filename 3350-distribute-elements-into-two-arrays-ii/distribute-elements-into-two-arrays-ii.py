from sortedcontainers import SortedList

class Solution:
    def greaterCounter(self, arr, val):
        # res = 0
        # for num in arr:
        #     if num > val:
        #         res += 1
        # return res
        index = bisect.bisect_right(arr, val)
        return len(arr) - index
    
    def resultArray(self, nums: List[int]) -> List[int]:
        if len(nums) <= 2:
            return nums
        
        arr1 = [nums[0]]
        arr2 = [nums[1]]
        oset1 = SortedList(arr1)
        oset2 = SortedList(arr2)

        
        for i in range(2, len(nums)):
            c1, c2 = self.greaterCounter(oset1, nums[i]), self.greaterCounter(oset2, nums[i])
            if c1 > c2:
                arr1.append(nums[i])
                oset1.add(nums[i])
            elif c1 == c2:
                if len(arr1) < len(arr2) or len(arr1) == len(arr2):
                    arr1.append(nums[i])
                    oset1.add(nums[i])
                else:
                    arr2.append(nums[i])
                    oset2.add(nums[i])
            else:
                arr2.append(nums[i])
                oset2.add(nums[i])
        
        return arr1 + arr2