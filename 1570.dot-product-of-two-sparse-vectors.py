#
# @lc app=leetcode id=1570 lang=python3
#
# [1570] Dot Product of Two Sparse Vectors
#

# @lc code=start
class SparseVector:
    def __init__(self, nums: List[int]):
        self.non_zero_elements = {i: num for i, num in enumerate(nums) if num != 0}

    # Return the dotProduct of two sparse vectors
    def dotProduct(self, vec: 'SparseVector') -> int:
        res = 0
        for i, val in self.non_zero_elements.items():
            if i in vec.non_zero_elements:
                res += val * vec.non_zero_elements[i]
        return res

# Your SparseVector object will be instantiated and called as such:
# v1 = SparseVector(nums1)
# v2 = SparseVector(nums2)
# ans = v1.dotProduct(v2)
# @lc code=end

