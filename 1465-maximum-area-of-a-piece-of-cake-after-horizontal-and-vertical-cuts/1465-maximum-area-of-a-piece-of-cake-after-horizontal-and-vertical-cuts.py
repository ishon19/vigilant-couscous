class Solution:
    def maxArea(self, h: int, w: int, hc: List[int], vc: List[int]) -> int:
        hc.sort()
        vc.sort()
        
        max_width = max(vc[0], w - vc[-1])
        for i in range(1, len(vc)):
            max_width = max(max_width, vc[i] - vc[i-1])
        
        max_height = max(hc[0], h - hc[-1])
        for i in range(1, len(hc)):
            max_height = max(max_height, hc[i] - hc[i-1])
        
        return (max_width * max_height) % (10**9 + 7)