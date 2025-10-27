class Solution:
    def areaOfMaxDiagonal(self, dimensions: List[List[int]]) -> int:
        get_diag = lambda x, y: x**2 + y**2
        area_list = sorted([(get_diag(x, y), x * y) for x, y in dimensions])
        return area_list[-1][-1]