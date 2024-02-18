class Solution:
    def findBuildings(self, heights: List[int]) -> List[int]:
        res = []
        stack = []

        for idx, height in reversed(list(enumerate(heights))):
            if not stack:
                stack.append(height)
                res.append(idx)
            else:
                while height > stack[-1]:
                    stack.pop()
                    stack.append(height)
                    res.append(idx)
        
        return sorted(res)