class Solution:
    def pivotIndex(self, nums: List[int]) -> int:
        total = sum(nums)
        print(total)
        for i in range(len(nums)):
            # print(total-nums[i])
            if (total-nums[i])%2==0:                
                left_sum = sum(nums[0:i])
                right_sum = sum(nums[i+1:len(nums)])
                print('pivot',i,'left sum',left_sum,'right sum',right_sum)
                if left_sum == right_sum:
                    return i                
        return -1