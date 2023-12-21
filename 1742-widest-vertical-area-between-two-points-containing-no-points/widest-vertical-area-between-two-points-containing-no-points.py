class Solution:
    def maxWidthOfVerticalArea(self, points: List[List[int]]) -> int:
        # sort the coordinates by the x-axis
        points.sort(key=lambda x: x[0])

        # print('sorted points', points)

        res = 0
        l, r = 0, 1
    
        while r<len(points):
            if points[l][0] == points[r][0]:
                l += 1
                r = l + 1
            else:
                res = max(res, points[r][0] - points[l][0])
                r += 1
                l += 1

        return res