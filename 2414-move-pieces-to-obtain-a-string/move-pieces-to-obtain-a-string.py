class Solution:
    def canChange(self, start: str, target: str) -> bool:
        start, target = list((i, c) for i, c in enumerate(start) if c != '_'), list((i, c) for i, c in enumerate(target) if c != '_')
        if len(start) != len(target):
            return False        
        for i in range(len(start)):
            if start[i][1] != target[i][1]:
                return False
            if start[i][1] == 'R' and start[i][0] > target[i][0]:
                return False
            if start[i][1] == 'L' and start[i][0] < target[i][0]:
                return False
        return True