#
# @lc app=leetcode id=986 lang=python3
#
# [986] Interval List Intersections
#

# @lc code=start
class Solution:
    def intervalIntersection(self, firstList: List[List[int]], secondList: List[List[int]]) -> List[List[int]]:
        # overlap starts at max(start1, start2) and ends at max(end1, end2)
        i, j = 0, 0
        res = []

        while i < len(firstList) and j < len(secondList):
            start1, end1 = firstList[i]
            start2, end2 = secondList[j]

            intersection_start = max(start1, start2)
            intersection_end = min(end1, end2)

            if intersection_start <= intersection_end:
                res.append([intersection_start, intersection_end])
            
            if end1 < end2:
                i += 1
            else:
                j += 1

        return res


# @lc code=end

