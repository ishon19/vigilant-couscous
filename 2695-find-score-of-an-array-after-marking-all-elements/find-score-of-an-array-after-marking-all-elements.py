class Solution:
    def findScore(self, nums: List[int]) -> int:
        score = 0
        heap = []
        marked = set()

        for i, num in enumerate(nums):
            heappush(heap, (num, i))
        
        while heap:
            lowest, idx = heappop(heap)
            if idx not in marked:
                # print((lowest, idx))
                score += lowest
                marked.add(idx)

                if 0<=idx + 1<len(nums) and idx + 1 not in marked:
                    marked.add(idx+1)
                
                if 0<= idx - 1<len(nums) and idx - 1 not in marked:
                    marked.add(idx-1)
            
            # print(marked)
            
        return score