class Solution:
    def minCost(self, colors: str, neededTime: List[int]) -> int:
        res = 0
        grpMax = 0
        colorList = list(colors)        

        for i in range(len(colorList)):
            if i > 0 and colorList[i-1] != colorList[i]:
                grpMax = 0
            
            res += min(grpMax, neededTime[i])
            grpMax = max(grpMax, neededTime[i])
        
        return res