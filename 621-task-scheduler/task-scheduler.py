class Solution:
    def leastInterval(self, tasks: List[str], n: int) -> int:
        counts = [-count for count in Counter(tasks).values()]
        heapify(counts)

        time = 0
        q = deque()

        while q or counts:
            time += 1

            if counts:
                freq = -heappop(counts) - 1
                if freq:
                    q.append((freq, time + n))
            else:
                # check the queue
                time = q[0][1]
            
            if q and q[0][1] == time:
                heappush(counts, -q.popleft()[0])
        
        return time