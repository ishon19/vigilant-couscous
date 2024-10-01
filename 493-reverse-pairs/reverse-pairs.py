class Solution:
    def reversePairs(self, nums: List[int]) -> int:
        # brute force
        # res = 0
        # for i in range(len(nums)):
        #     for j in range(len(nums)):                
        #         if i < j and nums[i] > 2 * nums[j]:
        #             res += 1        
        # return res

        # merge sort based comparison
        def merge_sort(left, right):
            if left >= right:
                return 0
            
            mid = (left + right) // 2
            count = merge_sort(left, mid) + merge_sort(mid + 1, right)

            # count pairs from left in right
            j = mid + 1
            for i in range(left, mid + 1):
                while j <= right and nums[i] > 2 * nums[j]:
                    j += 1
                count += j - (mid + 1)
            
            # merge
            nums[left: right+1] = sorted(nums[left: right+1])

            return count
        
        return merge_sort(0, len(nums) - 1)
