class Solution:
    def findDisappearedNumbers(self, nums: List[int]) -> List[int]:
        counts = {i+1: 0 for i in range(len(nums))}
        res = []
        for num in nums:
            counts[num] += 1

        for key in counts.keys():
            if not counts[key]:
                res.append(key)
        
        return res
