class Solution:
    def getRow(self, rowIndex: int) -> List[int]:
        if rowIndex <= 1:
            return [1]*(rowIndex+1)
        
        ans = [[1], [1,1]]
        for i in range(2, rowIndex+1):
            ans.append([1])
            for j in range(1,len(ans[i-1])):
                ans[i].append(ans[i-1][j] + ans[i-1][j-1])
            ans[i].append(1)
        
        return ans[rowIndex]
                
            