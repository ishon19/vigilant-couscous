class Solution:
    def minInterval(self, intervals: List[List[int]], queries: List[int]) -> List[int]:
        # start = sorted(intervals, key=lambda x: x[1]-x[0])
        # end = sorted(intervals, key=lambda x: x[1])
        # res = []
        # for query in queries:
        #     temp = float("inf")
        #     for i in range(len(start)):                
        #         if start[i][0]<=query<=start[i][1]:                    
        #             temp = min(temp, start[i][1]-start[i][0]+1)
        #             # print('found', query, start[i][0], start[i][1], temp)
        #     res.append(temp if temp!=float("inf") else -1)
        # return res
        intervals.sort()
        res, i = {}, 0
        minheap = []
        for query in sorted(queries):
            # push the smallest intervals in the min heap based on the starting value
            while i < len(intervals) and intervals[i][0] <= query:
                l, r = intervals[i]
                heapq.heappush(minheap, (r-l+1, r))
                i += 1
            
            while minheap and minheap[0][1] < query:
                heapq.heappop(minheap)
            
            res[query] = minheap[0][0] if minheap else -1

        return [res[q] for q in queries]