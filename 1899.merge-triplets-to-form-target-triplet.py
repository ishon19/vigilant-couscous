#
# @lc app=leetcode id=1899 lang=python3
#
# [1899] Merge Triplets to Form Target Triplet
#

# @lc code=start
class Solution:
    def mergeTriplets(self, triplets: List[List[int]], target: List[int]) -> bool:
        x_found = y_found = z_found = False

        for a, b, c in triplets:
            if a > target[0] or b > target[1] or c > target[2]:
                continue

            if a == target[0]:
                x_found = True
            if b == target[1]:
                y_found = True
            if c == target[2]:
                z_found = True
            
            if x_found and y_found and z_found:
                return True
        
        return False
# @lc code=end

