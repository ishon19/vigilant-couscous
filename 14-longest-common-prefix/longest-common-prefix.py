class Solution:
    def longestCommonPrefix(self, strs: List[str]) -> str:
        j = 0
        res = ''

        while True:
            temp = set()
            count = 0
            for i in range(len(strs)):
                if j < len(strs[i]):
                    temp.add(strs[i][j])
                    count += 1
                
            
            if len(temp) == 1 and count == len(strs) and j < len(strs[i]) and strs[0]:
                res += strs[0][j]
            else:
                break
            
            j += 1
        
        return res