class Solution:
    def minDifference(self, nums: List[int]) -> int:
        # if the array is <= 4 in size then we can set them all equal
        if len(nums) <= 4:
            return 0

        # three options to minimize the diff
        # sort first and make the last 3 equal
        # make the first three equal
        # make one from smallest and 2 from largest
        # two from smallest and one from the largest 
        # and take the min of those
        n = len(nums)
        nums.sort()
        opt1 = nums[n-4] - nums[0]
        opt2 = nums[n-3] - nums[1]
        opt3 = nums[n-2] - nums[2]
        opt4 = nums[n-1] - nums[3]

        return min(opt1, opt2, opt3,  opt4)