class Solution:
    def findMinArrowShots(self, points: List[List[int]]) -> int:        
        # def customMerge(points):
        #     if len(points) == 1:
        #         return points
        #     points.sort(key=lambda x: x[1])
        #     res = [points[0]]            
        #     for point in points[1:]:                
        #         if point[0] <= res[-1][1]:
        #             res[-1] = [min(point[0], res[-1][0]), min(point[1], res[-1][1])]
        #         else:
        #             res.append(point)
        #     print(res)
        #     return res        
        # return len(customMerge(points))

        points.sort(key=lambda x: x[0])
        res = [points[0]]

        for point in points[1:]:
            if res[-1][1] >= point[0]:
                res[-1] = [min(point[0], res[-1][0]), min(point[1], res[-1][1])]
            else:
                res.append(point)
        
        return len(res)
