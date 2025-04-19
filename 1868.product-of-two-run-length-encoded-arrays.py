#
# @lc app=leetcode id=1868 lang=python3
#
# [1868] Product of Two Run-Length Encoded Arrays
#

# @lc code=start
class Solution:
    def findRLEArray(self, encoded1: List[List[int]], encoded2: List[List[int]]) -> List[List[int]]:
        res = []
        i = j = 0

        while i < len(encoded1) and j < len(encoded2):
            val1, freq1 = encoded1[i]
            val2, freq2 = encoded2[j]

            product = val1 * val2
            freq = min(freq1, freq2)

            if res and res[-1][0] == product:
                res[-1][-1] += freq
            else:
                res.append([product, freq])
            
            encoded1[i][1] -= freq
            encoded2[j][1] -= freq

            if encoded1[i][1] == 0:
                i += 1
            if encoded2[j][1] == 0:
                j += 1
        
        return res
# @lc code=end

