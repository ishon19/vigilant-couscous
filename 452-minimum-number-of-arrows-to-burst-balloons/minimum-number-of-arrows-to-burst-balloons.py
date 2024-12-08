class Solution:
    def findMinArrowShots(self, points: List[List[int]]) -> int:        
        points.sort()
        res = []

        for point in points:
            if res and res[-1][1] >= point[0]:
                res[-1] = [max(res[-1][0], point[0]), min(res[-1][1], point[1])]
            else:
                res.append(point)
        print(res)
        return len(res)
