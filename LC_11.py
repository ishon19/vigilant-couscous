class Solution:
    def maxArea(self, height: List[int]) -> int:
        if len(height) == 2:
            return min(height[0], height[1])
        area, left, right = 0, 0, len(height) - 1
        while left != right:
            curr_area = min(height[left], height[right]) * (right-left)
            area = max(area, curr_area)
            if height[left] < height[right]:
                left += 1
            else:
                right -= 1
        return area
            