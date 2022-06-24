class Solution:
    def generate(self, numRows: int) -> List[List[int]]:                        
        ans = []
        for i in range(numRows):
            temp = [0] * (i+1)
            temp[0] = 1
            for j in range(1,i):                
                temp[j] = ans[i-1][j] + ans[i-1][j-1]
            temp[i] = 1
            ans.append(temp)            
        return ans