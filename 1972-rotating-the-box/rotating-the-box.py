class Solution:
    def rotate(self, box):
        transpose = list(zip(*box))
        return [list(reversed(row)) for row in transpose]

    def rotateTheBox(self, box: List[List[str]]) -> List[List[str]]:
        rows, cols = len(box), len(box[0])
        
        for row in range(rows):
            lastFree = cols - 1
            for i in range(cols-1,-1,-1):
                if box[row][i] == '*':
                    lastFree = i - 1
                elif box[row][i] == '#':
                    box[row][i], box[row][lastFree] = '.', '#'
                    lastFree -= 1
        
        return self.rotate(box)