class Solution:
    def findBuildings(self, heights: List[int]) -> List[int]:
        stack = []

        for i, height in enumerate(heights):
            while stack and stack[-1][1] <= height:
                stack.pop()
            stack.append((i, height))
        
        return [i for i, _ in stack]