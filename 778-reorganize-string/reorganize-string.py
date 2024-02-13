class Solution:
    def reorganizeString(self, s: str) -> str:
        # editorial Solution

        # use pq to get the letter with top count
        res = ''

        # negated the count to emulate the max heap
        q = [(-count, char) for char, count in collections.Counter(s).items()]
        heapq.heapify(q)

        while q:
            top_count, top_char = heapq.heappop(q)
            if not res or top_char != res[-1]:
                # if its a new char
                res += top_char

                # since count has to be decreased from a negative number, we add
                if top_count + 1 != 0:
                    heapq.heappush(q, (top_count + 1, top_char))
            else:
                # we use the other char, as we can not use the same one twice
                if not q: return ''

                other_count, other_char = heapq.heappop(q)
                res += other_char
                if other_count + 1 != 0:
                    heapq.heappush(q, (other_count + 1, other_char))
                heapq.heappush(q, (top_count, top_char))
        
        return res
                
