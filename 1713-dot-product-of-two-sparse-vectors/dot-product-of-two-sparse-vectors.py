class SparseVector:
    def __init__(self, nums: List[int]):
        self.vector = nums

    # Return the dotProduct of two sparse vectors
    def dotProduct(self, vec: 'SparseVector') -> int:
        v1 = self.vector
        v2 = vec.vector

        if not v1 and not v2: return 0
        if v1 and not v2: return v1
        if v2 and not v1: return v2
        
        return sum(i * j for i, j in zip(v1, v2))

# Your SparseVector object will be instantiated and called as such:
# v1 = SparseVector(nums1)
# v2 = SparseVector(nums2)
# ans = v1.dotProduct(v2)