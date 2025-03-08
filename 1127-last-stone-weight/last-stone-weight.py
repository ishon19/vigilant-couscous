class Solution:
    def lastStoneWeight(self, stones: List[int]) -> int:
        stones = [-weight for weight in stones]
        heapify(stones)

        while len(stones)>1:
            a = heappop(stones)
            b = heappop(stones)

            if a == b:
                continue
            else:
                heappush(stones, a-b)
        
        return -stones[0] if stones else 0