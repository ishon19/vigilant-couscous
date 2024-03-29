class Solution:
    def countSubarrays(self, nums: List[int], k: int) -> int:
        window_elements = 0
        start = 0
        res = 0
        max_element = max(nums)

        for end in range(len(nums)):
            if nums[end] == max_element:
                window_elements += 1
            
            while window_elements == k:
                if nums[start] == max_element:
                    window_elements -= 1
                start += 1
            res += start
        return res
            