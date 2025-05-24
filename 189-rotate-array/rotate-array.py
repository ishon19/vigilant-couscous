class Solution:
    def rotate(self, nums: List[int], k: int) -> None:
        """
        Do not return anything, modify nums in-place instead.
        """
        k = k % len(nums)

        def reverse(arr, left, right):
            while left <= right:
                arr[left], arr[right] = arr[right], arr[left]
                left += 1
                right -= 1
            return arr 
        
        reverse(nums, 0, len(nums)-1)
        reverse(nums, 0, k-1)
        reverse(nums, k, len(nums)-1)
            