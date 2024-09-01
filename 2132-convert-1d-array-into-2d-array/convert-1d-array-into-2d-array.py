class Solution:
    def construct2DArray(self, original: List[int], m: int, n: int) -> List[List[int]]:
        # res = []
        # if m * n == len(original):
        #     i, j = 0, n-1
        #     while len(res) != m:
        #         res.append(original[i:j+1])
        #         i += n
        #         j += n
        # return res

        rows, cols = m, n
        if m * n != len(original):
            return []

        grid = []
        idx = 0
        for i in range(rows):
            row = []
            if idx >= len(original): break
            for j in range(cols):
                if idx + j < len(original): row.append(original[idx + j])
            idx += cols
            grid.append(row)
        
        return grid