class Solution:
    def generatePossibleNextMoves(self, currentState: str) -> List[str]:
        if len(currentState) < 2:
            return []

        l, r = 0, 2
        res = []

        while r<=len(currentState):
            if currentState[l:r] == "++":
                res.append(currentState[:l] + "--" + currentState[r:])
            r += 1
            l += 1
        
        return res

