class Solution:
    def minGroups(self, intervals: List[List[int]]) -> int:
        # use the priority queue to determine the grouping
        pq = []

        for left, right in sorted(intervals):
            if pq and pq[0] < left:
                heappop(pq)
            heappush(pq, right)

        return len(pq)
