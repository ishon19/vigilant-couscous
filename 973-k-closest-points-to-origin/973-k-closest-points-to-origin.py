class Solution:
    def kClosest(self, points: List[List[int]], k: int) -> List[List[int]]:
        temp = [[(i**2+j**2), i, j] for i,j in points]        
        heapq.heapify(temp)
        res = []

        while k>0:            
            dist, i, j = heapq.heappop(temp)
            res.append([i,j])
            k -= 1
        return res