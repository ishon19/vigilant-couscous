class Solution:
    def findBuildings(self, heights: List[int]) -> List[int]:
        stack = []

        for i, height in enumerate(heights):
            while stack and stack[-1][-1] <= height:
                stack.pop()
            else:
                stack.append([i, height])
        
        return [idx for idx, _ in stack]